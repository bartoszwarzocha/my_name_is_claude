#!/usr/bin/env python3
"""
AI-Powered Agent Selection - Ensemble ML Models
Claude Code Multi-Agent Framework Enhancement

This module implements ensemble machine learning models for intelligent
agent recommendation based on project context analysis.

Components:
- Random Forest-style Decision Tree Ensemble
- Neural Network-style Multi-layer Perceptron
- Rule-based Business Logic Validator
- Ensemble Coordination and Weighted Voting
- Model Performance Tracking and Optimization

Version: 1.0.0
Phase: 1 - Foundation Development
Note: Simplified implementation without external ML dependencies
"""

import json
import math
import random
import logging
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod
from pathlib import Path
import pickle

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentRecommendation:
    """Single agent recommendation with confidence and rationale"""
    agent_name: str
    confidence_score: float
    reasoning: List[str]
    feature_importance: Dict[str, float]
    alternative_agents: List[str]

@dataclass
class RecommendationResult:
    """Complete recommendation result from ensemble"""
    primary_recommendations: List[AgentRecommendation]
    workflow_sequence: List[str]
    confidence_threshold: float
    model_performance: Dict[str, float]
    explanation: str

@dataclass
class TrainingData:
    """Training data structure for ML models"""
    project_features: List[List[float]]
    agent_selections: List[List[str]]
    success_metrics: List[float]
    metadata: List[Dict[str, Any]]

class MLModel(ABC):
    """Abstract base class for ML models"""

    @abstractmethod
    def train(self, training_data: TrainingData):
        """Train the model"""
        pass

    @abstractmethod
    def predict(self, features: List[float]) -> Dict[str, float]:
        """Predict agent recommendations"""
        pass

    @abstractmethod
    def get_feature_importance(self) -> Dict[str, float]:
        """Get feature importance scores"""
        pass

class SimplifiedRandomForest(MLModel):
    """Simplified Random Forest implementation for agent recommendation"""

    def __init__(self, n_trees: int = 10, max_depth: int = 5):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []
        self.agent_names = []
        self.feature_importance = {}
        self.is_trained = False

    def train(self, training_data: TrainingData):
        """Train the random forest ensemble"""
        logger.info(f"Training Random Forest with {self.n_trees} trees")

        if not training_data.project_features:
            raise ValueError("No training data provided")

        # Extract unique agent names
        all_agents = set()
        for selection in training_data.agent_selections:
            all_agents.update(selection)
        self.agent_names = sorted(list(all_agents))

        # Convert agent selections to binary vectors
        y_binary = self._convert_to_binary_labels(training_data.agent_selections)

        # Train each tree
        self.trees = []
        for i in range(self.n_trees):
            tree = self._train_single_tree(training_data.project_features, y_binary, i)
            self.trees.append(tree)

        # Calculate feature importance
        self._calculate_feature_importance(training_data.project_features)
        self.is_trained = True

        logger.info(f"Random Forest training complete. {len(self.agent_names)} agents.")

    def predict(self, features: List[float]) -> Dict[str, float]:
        """Predict agent recommendations using ensemble voting"""
        if not self.is_trained:
            raise ValueError("Model must be trained before prediction")

        agent_scores = {agent: 0.0 for agent in self.agent_names}

        # Get predictions from each tree
        for tree in self.trees:
            tree_predictions = self._predict_single_tree(tree, features)
            for agent, score in tree_predictions.items():
                agent_scores[agent] += score

        # Average across trees
        for agent in agent_scores:
            agent_scores[agent] /= len(self.trees)

        return agent_scores

    def get_feature_importance(self) -> Dict[str, float]:
        """Get feature importance scores"""
        return self.feature_importance.copy()

    def _convert_to_binary_labels(self, agent_selections: List[List[str]]) -> List[List[int]]:
        """Convert agent selections to binary vectors"""
        binary_labels = []
        for selection in agent_selections:
            binary_vector = [1 if agent in selection else 0 for agent in self.agent_names]
            binary_labels.append(binary_vector)
        return binary_labels

    def _train_single_tree(self, X: List[List[float]], y: List[List[int]], seed: int) -> Dict[str, Any]:
        """Train a single decision tree"""
        random.seed(seed)

        # Bootstrap sampling
        n_samples = len(X)
        bootstrap_indices = [random.randint(0, n_samples - 1) for _ in range(n_samples)]
        bootstrap_X = [X[i] for i in bootstrap_indices]
        bootstrap_y = [y[i] for i in bootstrap_indices]

        # Build decision tree (simplified)
        tree = self._build_tree(bootstrap_X, bootstrap_y, depth=0)
        return tree

    def _build_tree(self, X: List[List[float]], y: List[List[int]], depth: int) -> Dict[str, Any]:
        """Build a single decision tree node"""
        if depth >= self.max_depth or len(X) < 2:
            # Leaf node - return average predictions
            avg_predictions = [0.0] * len(self.agent_names)
            for label_vector in y:
                for i, label in enumerate(label_vector):
                    avg_predictions[i] += label

            for i in range(len(avg_predictions)):
                avg_predictions[i] /= len(y)

            return {
                'type': 'leaf',
                'predictions': {self.agent_names[i]: avg_predictions[i] for i in range(len(self.agent_names))}
            }

        # Find best split
        best_feature, best_threshold, best_score = self._find_best_split(X, y)

        if best_feature is None:
            # No good split found, return leaf
            avg_predictions = [sum(label_vector[i] for label_vector in y) / len(y) for i in range(len(self.agent_names))]
            return {
                'type': 'leaf',
                'predictions': {self.agent_names[i]: avg_predictions[i] for i in range(len(self.agent_names))}
            }

        # Split data
        left_X, left_y, right_X, right_y = self._split_data(X, y, best_feature, best_threshold)

        # Recursively build subtrees
        left_tree = self._build_tree(left_X, left_y, depth + 1)
        right_tree = self._build_tree(right_X, right_y, depth + 1)

        return {
            'type': 'split',
            'feature': best_feature,
            'threshold': best_threshold,
            'left': left_tree,
            'right': right_tree
        }

    def _find_best_split(self, X: List[List[float]], y: List[List[int]]) -> Tuple[Optional[int], Optional[float], float]:
        """Find the best feature and threshold for splitting"""
        best_feature = None
        best_threshold = None
        best_score = float('inf')

        n_features = len(X[0]) if X else 0
        n_features_to_try = max(1, int(math.sqrt(n_features)))

        # Randomly select features to try
        features_to_try = random.sample(range(n_features), min(n_features_to_try, n_features))

        for feature_idx in features_to_try:
            # Get unique values for this feature
            feature_values = list(set(row[feature_idx] for row in X))

            for threshold in feature_values:
                score = self._calculate_split_score(X, y, feature_idx, threshold)

                if score < best_score:
                    best_score = score
                    best_feature = feature_idx
                    best_threshold = threshold

        return best_feature, best_threshold, best_score

    def _calculate_split_score(self, X: List[List[float]], y: List[List[int]], feature_idx: int, threshold: float) -> float:
        """Calculate the quality score for a split (lower is better)"""
        left_y = []
        right_y = []

        for i, row in enumerate(X):
            if row[feature_idx] <= threshold:
                left_y.append(y[i])
            else:
                right_y.append(y[i])

        if not left_y or not right_y:
            return float('inf')  # Bad split

        # Calculate impurity (simplified Gini impurity)
        left_impurity = self._calculate_gini_impurity(left_y)
        right_impurity = self._calculate_gini_impurity(right_y)

        # Weighted average impurity
        total_samples = len(y)
        left_weight = len(left_y) / total_samples
        right_weight = len(right_y) / total_samples

        weighted_impurity = left_weight * left_impurity + right_weight * right_impurity
        return weighted_impurity

    def _calculate_gini_impurity(self, y: List[List[int]]) -> float:
        """Calculate Gini impurity for a set of labels"""
        if not y:
            return 0.0

        # For multi-label case, calculate average Gini across all agents
        n_agents = len(self.agent_names)
        total_impurity = 0.0

        for agent_idx in range(n_agents):
            positive_count = sum(1 for label_vector in y if label_vector[agent_idx] == 1)
            total_count = len(y)

            if total_count == 0:
                continue

            p_positive = positive_count / total_count
            p_negative = 1 - p_positive

            gini = 1 - (p_positive ** 2 + p_negative ** 2)
            total_impurity += gini

        return total_impurity / n_agents

    def _split_data(self, X: List[List[float]], y: List[List[int]], feature_idx: int, threshold: float) -> Tuple[List[List[float]], List[List[int]], List[List[float]], List[List[int]]]:
        """Split data based on feature and threshold"""
        left_X, left_y = [], []
        right_X, right_y = [], []

        for i, row in enumerate(X):
            if row[feature_idx] <= threshold:
                left_X.append(row)
                left_y.append(y[i])
            else:
                right_X.append(row)
                right_y.append(y[i])

        return left_X, left_y, right_X, right_y

    def _predict_single_tree(self, tree: Dict[str, Any], features: List[float]) -> Dict[str, float]:
        """Predict using a single tree"""
        current_node = tree

        while current_node['type'] == 'split':
            feature_idx = current_node['feature']
            threshold = current_node['threshold']

            if features[feature_idx] <= threshold:
                current_node = current_node['left']
            else:
                current_node = current_node['right']

        return current_node['predictions']

    def _calculate_feature_importance(self, X: List[List[float]]):
        """Calculate feature importance based on usage in splits"""
        if not X:
            return

        n_features = len(X[0])
        feature_counts = [0] * n_features

        # Count how often each feature is used in splits
        for tree in self.trees:
            self._count_feature_usage(tree, feature_counts)

        # Normalize to get importance scores
        total_usage = sum(feature_counts)
        if total_usage > 0:
            self.feature_importance = {
                f"feature_{i}": count / total_usage
                for i, count in enumerate(feature_counts)
            }
        else:
            self.feature_importance = {f"feature_{i}": 0.0 for i in range(n_features)}

    def _count_feature_usage(self, node: Dict[str, Any], feature_counts: List[int]):
        """Recursively count feature usage in tree"""
        if node['type'] == 'split':
            feature_counts[node['feature']] += 1
            self._count_feature_usage(node['left'], feature_counts)
            self._count_feature_usage(node['right'], feature_counts)

class SimplifiedNeuralNetwork(MLModel):
    """Simplified Neural Network implementation for agent recommendation"""

    def __init__(self, hidden_layers: List[int] = [64, 32]):
        self.hidden_layers = hidden_layers
        self.weights = []
        self.biases = []
        self.agent_names = []
        self.feature_importance = {}
        self.is_trained = False
        self.learning_rate = 0.01
        self.epochs = 100

    def train(self, training_data: TrainingData):
        """Train the neural network"""
        logger.info(f"Training Neural Network with layers: {self.hidden_layers}")

        if not training_data.project_features:
            raise ValueError("No training data provided")

        # Extract unique agent names
        all_agents = set()
        for selection in training_data.agent_selections:
            all_agents.update(selection)
        self.agent_names = sorted(list(all_agents))

        # Convert to training format
        X = training_data.project_features
        y = self._convert_to_binary_labels(training_data.agent_selections)

        # Initialize network architecture
        self._initialize_network(len(X[0]), len(self.agent_names))

        # Train using simplified gradient descent
        self._train_network(X, y)

        # Calculate feature importance (simplified)
        self._calculate_feature_importance()
        self.is_trained = True

        logger.info(f"Neural Network training complete. {len(self.agent_names)} agents.")

    def predict(self, features: List[float]) -> Dict[str, float]:
        """Predict agent recommendations using neural network"""
        if not self.is_trained:
            raise ValueError("Model must be trained before prediction")

        # Forward pass
        output = self._forward_pass(features)

        # Convert to agent scores
        agent_scores = {self.agent_names[i]: output[i] for i in range(len(self.agent_names))}
        return agent_scores

    def get_feature_importance(self) -> Dict[str, float]:
        """Get feature importance scores"""
        return self.feature_importance.copy()

    def _convert_to_binary_labels(self, agent_selections: List[List[str]]) -> List[List[float]]:
        """Convert agent selections to binary vectors"""
        binary_labels = []
        for selection in agent_selections:
            binary_vector = [1.0 if agent in selection else 0.0 for agent in self.agent_names]
            binary_labels.append(binary_vector)
        return binary_labels

    def _initialize_network(self, input_size: int, output_size: int):
        """Initialize network weights and biases"""
        layer_sizes = [input_size] + self.hidden_layers + [output_size]

        self.weights = []
        self.biases = []

        for i in range(len(layer_sizes) - 1):
            # Xavier initialization
            fan_in = layer_sizes[i]
            fan_out = layer_sizes[i + 1]
            limit = math.sqrt(6.0 / (fan_in + fan_out))

            weight_matrix = [
                [random.uniform(-limit, limit) for _ in range(fan_out)]
                for _ in range(fan_in)
            ]
            bias_vector = [0.0] * fan_out

            self.weights.append(weight_matrix)
            self.biases.append(bias_vector)

    def _train_network(self, X: List[List[float]], y: List[List[float]]):
        """Train network using simplified gradient descent"""
        n_samples = len(X)

        for epoch in range(self.epochs):
            total_loss = 0.0

            for i in range(n_samples):
                # Forward pass
                activations = self._forward_pass_detailed(X[i])

                # Calculate loss
                output = activations[-1]
                loss = self._calculate_loss(output, y[i])
                total_loss += loss

                # Backward pass (simplified)
                self._backward_pass(activations, y[i])

            if epoch % 20 == 0:
                avg_loss = total_loss / n_samples
                logger.debug(f"Epoch {epoch}, Average Loss: {avg_loss:.4f}")

    def _forward_pass(self, inputs: List[float]) -> List[float]:
        """Forward pass through network"""
        current_values = inputs[:]

        for layer_idx in range(len(self.weights)):
            next_values = []
            weights = self.weights[layer_idx]
            biases = self.biases[layer_idx]

            for output_idx in range(len(biases)):
                weighted_sum = biases[output_idx]
                for input_idx in range(len(current_values)):
                    weighted_sum += current_values[input_idx] * weights[input_idx][output_idx]

                # Activation function (sigmoid for hidden layers, sigmoid for output)
                activated_value = self._sigmoid(weighted_sum)
                next_values.append(activated_value)

            current_values = next_values

        return current_values

    def _forward_pass_detailed(self, inputs: List[float]) -> List[List[float]]:
        """Forward pass that returns all layer activations"""
        activations = [inputs[:]]

        current_values = inputs[:]
        for layer_idx in range(len(self.weights)):
            next_values = []
            weights = self.weights[layer_idx]
            biases = self.biases[layer_idx]

            for output_idx in range(len(biases)):
                weighted_sum = biases[output_idx]
                for input_idx in range(len(current_values)):
                    weighted_sum += current_values[input_idx] * weights[input_idx][output_idx]

                activated_value = self._sigmoid(weighted_sum)
                next_values.append(activated_value)

            current_values = next_values
            activations.append(current_values[:])

        return activations

    def _backward_pass(self, activations: List[List[float]], targets: List[float]):
        """Simplified backward pass for weight updates"""
        # Calculate output layer error
        output = activations[-1]
        output_errors = [
            (targets[i] - output[i]) * self._sigmoid_derivative(output[i])
            for i in range(len(output))
        ]

        # Update weights (simplified, only output layer)
        if len(self.weights) > 0:
            # Update output layer weights
            layer_idx = len(self.weights) - 1
            prev_activations = activations[layer_idx]

            for i in range(len(prev_activations)):
                for j in range(len(output_errors)):
                    gradient = prev_activations[i] * output_errors[j]
                    self.weights[layer_idx][i][j] += self.learning_rate * gradient

            # Update output layer biases
            for j in range(len(output_errors)):
                self.biases[layer_idx][j] += self.learning_rate * output_errors[j]

    def _sigmoid(self, x: float) -> float:
        """Sigmoid activation function"""
        return 1.0 / (1.0 + math.exp(-max(-500, min(500, x))))  # Clamp to prevent overflow

    def _sigmoid_derivative(self, sigmoid_output: float) -> float:
        """Derivative of sigmoid function"""
        return sigmoid_output * (1.0 - sigmoid_output)

    def _calculate_loss(self, predictions: List[float], targets: List[float]) -> float:
        """Calculate mean squared error loss"""
        total_loss = 0.0
        for i in range(len(predictions)):
            error = predictions[i] - targets[i]
            total_loss += error * error
        return total_loss / len(predictions)

    def _calculate_feature_importance(self):
        """Calculate feature importance based on first layer weights"""
        if not self.weights:
            return

        input_weights = self.weights[0]
        n_features = len(input_weights)

        # Calculate average absolute weight for each input feature
        feature_scores = []
        for feature_idx in range(n_features):
            total_weight = sum(abs(input_weights[feature_idx][output_idx])
                             for output_idx in range(len(input_weights[feature_idx])))
            feature_scores.append(total_weight)

        # Normalize
        total_score = sum(feature_scores)
        if total_score > 0:
            self.feature_importance = {
                f"feature_{i}": score / total_score
                for i, score in enumerate(feature_scores)
            }
        else:
            self.feature_importance = {f"feature_{i}": 0.0 for i in range(n_features)}

class RuleBasedValidator(MLModel):
    """Rule-based business logic validator for agent recommendations"""

    def __init__(self):
        self.rules = []
        self.agent_names = []
        self.feature_importance = {}
        self.is_trained = False

    def train(self, training_data: TrainingData):
        """Learn rules from training data"""
        logger.info("Training Rule-based Validator")

        # Extract unique agent names
        all_agents = set()
        for selection in training_data.agent_selections:
            all_agents.update(selection)
        self.agent_names = sorted(list(all_agents))

        # Define business rules (simplified)
        self.rules = self._define_business_rules()

        # Simple feature importance (equal weights for rule-based features)
        n_features = len(training_data.project_features[0]) if training_data.project_features else 0
        self.feature_importance = {f"feature_{i}": 1.0 / max(1, n_features) for i in range(n_features)}

        self.is_trained = True
        logger.info(f"Rule-based Validator training complete. {len(self.rules)} rules defined.")

    def predict(self, features: List[float]) -> Dict[str, float]:
        """Apply business rules to recommend agents"""
        if not self.is_trained:
            raise ValueError("Model must be trained before prediction")

        agent_scores = {agent: 0.0 for agent in self.agent_names}

        # Apply each rule
        for rule in self.rules:
            rule_result = self._apply_rule(rule, features)
            for agent, score in rule_result.items():
                if agent in agent_scores:
                    agent_scores[agent] = max(agent_scores[agent], score)

        return agent_scores

    def get_feature_importance(self) -> Dict[str, float]:
        """Get feature importance scores"""
        return self.feature_importance.copy()

    def _define_business_rules(self) -> List[Dict[str, Any]]:
        """Define business logic rules for agent selection"""
        rules = [
            {
                'name': 'frontend_technology_rule',
                'condition': lambda f: self._has_frontend_tech(f),
                'agents': {'frontend-engineer': 0.9},
                'description': 'Recommend frontend engineer for frontend technologies'
            },
            {
                'name': 'backend_technology_rule',
                'condition': lambda f: self._has_backend_tech(f),
                'agents': {'backend-engineer': 0.9, 'api-engineer': 0.7},
                'description': 'Recommend backend engineers for backend technologies'
            },
            {
                'name': 'database_technology_rule',
                'condition': lambda f: self._has_database_tech(f),
                'agents': {'data-engineer': 0.8, 'database-administrator': 0.7},
                'description': 'Recommend data engineers for database technologies'
            },
            {
                'name': 'infrastructure_rule',
                'condition': lambda f: self._has_infrastructure_tech(f),
                'agents': {'deployment-engineer': 0.8, 'platform-engineer': 0.6},
                'description': 'Recommend deployment engineers for infrastructure'
            },
            {
                'name': 'enterprise_complexity_rule',
                'condition': lambda f: self._is_enterprise_project(f),
                'agents': {'enterprise-architect': 0.8, 'security-engineer': 0.7, 'compliance-auditor': 0.6},
                'description': 'Recommend enterprise agents for complex projects'
            },
            {
                'name': 'security_compliance_rule',
                'condition': lambda f: self._has_compliance_requirements(f),
                'agents': {'security-engineer': 0.9, 'compliance-auditor': 0.8},
                'description': 'Recommend security agents for compliance requirements'
            },
            {
                'name': 'testing_rule',
                'condition': lambda f: self._has_testing_tech(f),
                'agents': {'qa-engineer': 0.8},
                'description': 'Recommend QA engineer for testing technologies'
            },
            {
                'name': 'always_project_management_rule',
                'condition': lambda f: True,  # Always apply
                'agents': {'project-owner': 0.95, 'session-manager': 0.9},
                'description': 'Always recommend core project management agents'
            }
        ]

        return rules

    def _apply_rule(self, rule: Dict[str, Any], features: List[float]) -> Dict[str, float]:
        """Apply a single rule to features"""
        try:
            if rule['condition'](features):
                return rule['agents']
        except Exception as e:
            logger.debug(f"Error applying rule {rule['name']}: {e}")

        return {}

    def _has_frontend_tech(self, features: List[float]) -> bool:
        """Check if project has frontend technologies (simplified check)"""
        # This is a simplified check - in real implementation,
        # this would map to specific feature indices
        return len(features) > 10 and features[0] > 0.5  # Mock check

    def _has_backend_tech(self, features: List[float]) -> bool:
        """Check if project has backend technologies"""
        return len(features) > 15 and features[5] > 0.5  # Mock check

    def _has_database_tech(self, features: List[float]) -> bool:
        """Check if project has database technologies"""
        return len(features) > 20 and features[10] > 0.5  # Mock check

    def _has_infrastructure_tech(self, features: List[float]) -> bool:
        """Check if project has infrastructure technologies"""
        return len(features) > 25 and features[15] > 0.5  # Mock check

    def _is_enterprise_project(self, features: List[float]) -> bool:
        """Check if project is enterprise-scale"""
        return len(features) > 30 and features[20] > 0.7  # Mock check

    def _has_compliance_requirements(self, features: List[float]) -> bool:
        """Check if project has compliance requirements"""
        return len(features) > 35 and features[25] > 0.6  # Mock check

    def _has_testing_tech(self, features: List[float]) -> bool:
        """Check if project has testing technologies"""
        return len(features) > 40 and features[30] > 0.5  # Mock check

class EnsembleAgentRecommender:
    """Ensemble coordinator for agent recommendation models"""

    def __init__(self, model_weights: Optional[Dict[str, float]] = None):
        self.models = {}
        self.model_weights = model_weights or {
            'random_forest': 0.4,
            'neural_network': 0.4,
            'rule_based': 0.2
        }
        self.is_trained = False
        self.performance_metrics = {}

    def add_model(self, name: str, model: MLModel):
        """Add a model to the ensemble"""
        self.models[name] = model
        logger.info(f"Added model to ensemble: {name}")

    def train(self, training_data: TrainingData):
        """Train all models in the ensemble"""
        logger.info("Training ensemble models...")

        if not self.models:
            raise ValueError("No models added to ensemble")

        for name, model in self.models.items():
            logger.info(f"Training {name}...")
            try:
                model.train(training_data)
                logger.info(f"✅ {name} training completed")
            except Exception as e:
                logger.error(f"❌ Error training {name}: {e}")

        self.is_trained = True
        logger.info("🎯 Ensemble training completed")

    def recommend_agents(self, features: List[float], confidence_threshold: float = 0.5) -> RecommendationResult:
        """Generate agent recommendations using ensemble"""
        if not self.is_trained:
            raise ValueError("Ensemble must be trained before making recommendations")

        # Get predictions from each model
        model_predictions = {}
        for name, model in self.models.items():
            try:
                predictions = model.predict(features)
                model_predictions[name] = predictions
            except Exception as e:
                logger.warning(f"Error getting predictions from {name}: {e}")
                model_predictions[name] = {}

        # Combine predictions using weighted voting
        ensemble_scores = self._combine_predictions(model_predictions)

        # Filter by confidence threshold
        high_confidence_agents = {
            agent: score for agent, score in ensemble_scores.items()
            if score >= confidence_threshold
        }

        # Generate recommendations
        recommendations = self._generate_recommendations(
            ensemble_scores, high_confidence_agents, model_predictions
        )

        # Generate workflow sequence
        workflow_sequence = self._generate_workflow_sequence(high_confidence_agents)

        # Calculate model performance metrics
        performance = self._calculate_ensemble_performance(model_predictions)

        # Generate explanation
        explanation = self._generate_explanation(ensemble_scores, model_predictions)

        return RecommendationResult(
            primary_recommendations=recommendations,
            workflow_sequence=workflow_sequence,
            confidence_threshold=confidence_threshold,
            model_performance=performance,
            explanation=explanation
        )

    def _combine_predictions(self, model_predictions: Dict[str, Dict[str, float]]) -> Dict[str, float]:
        """Combine predictions from multiple models using weighted voting"""
        all_agents = set()
        for predictions in model_predictions.values():
            all_agents.update(predictions.keys())

        ensemble_scores = {}
        for agent in all_agents:
            weighted_score = 0.0
            total_weight = 0.0

            for model_name, predictions in model_predictions.items():
                if agent in predictions:
                    weight = self.model_weights.get(model_name, 0.0)
                    weighted_score += predictions[agent] * weight
                    total_weight += weight

            if total_weight > 0:
                ensemble_scores[agent] = weighted_score / total_weight
            else:
                ensemble_scores[agent] = 0.0

        return ensemble_scores

    def _generate_recommendations(self, ensemble_scores: Dict[str, float],
                                high_confidence_agents: Dict[str, float],
                                model_predictions: Dict[str, Dict[str, float]]) -> List[AgentRecommendation]:
        """Generate detailed agent recommendations"""
        recommendations = []

        # Sort agents by confidence score
        sorted_agents = sorted(ensemble_scores.items(), key=lambda x: x[1], reverse=True)

        for agent_name, confidence_score in sorted_agents[:10]:  # Top 10 recommendations
            # Generate reasoning
            reasoning = self._generate_reasoning(agent_name, confidence_score, model_predictions)

            # Calculate feature importance (simplified)
            feature_importance = self._get_agent_feature_importance(agent_name)

            # Find alternative agents
            alternatives = [name for name, score in sorted_agents
                          if name != agent_name and score > 0.3][:3]

            recommendation = AgentRecommendation(
                agent_name=agent_name,
                confidence_score=confidence_score,
                reasoning=reasoning,
                feature_importance=feature_importance,
                alternative_agents=alternatives
            )

            recommendations.append(recommendation)

        return recommendations

    def _generate_reasoning(self, agent_name: str, confidence_score: float,
                          model_predictions: Dict[str, Dict[str, float]]) -> List[str]:
        """Generate reasoning for agent recommendation"""
        reasoning = []

        # Check which models recommended this agent
        recommending_models = []
        for model_name, predictions in model_predictions.items():
            if agent_name in predictions and predictions[agent_name] > 0.5:
                recommending_models.append(model_name)

        if recommending_models:
            reasoning.append(f"Recommended by {len(recommending_models)} model(s): {', '.join(recommending_models)}")

        # Confidence level reasoning
        if confidence_score > 0.8:
            reasoning.append("High confidence based on strong feature alignment")
        elif confidence_score > 0.6:
            reasoning.append("Medium confidence with good project compatibility")
        else:
            reasoning.append("Lower confidence, consider as secondary option")

        # Agent-specific reasoning (simplified)
        agent_reasoning = {
            'frontend-engineer': "Project shows frontend technology indicators",
            'backend-engineer': "Backend development patterns detected",
            'api-engineer': "API integration requirements identified",
            'data-engineer': "Database and data processing needs",
            'security-engineer': "Security and compliance requirements detected",
            'qa-engineer': "Testing and quality assurance needs",
            'project-owner': "Essential for project coordination and management",
            'session-manager': "Required for framework session management"
        }

        if agent_name in agent_reasoning:
            reasoning.append(agent_reasoning[agent_name])

        return reasoning

    def _get_agent_feature_importance(self, agent_name: str) -> Dict[str, float]:
        """Get feature importance for specific agent (simplified)"""
        # This is a simplified implementation
        # In a real system, this would analyze which features most influence this agent's selection
        return {
            'technology_stack': 0.4,
            'project_complexity': 0.3,
            'business_domain': 0.2,
            'team_context': 0.1
        }

    def _generate_workflow_sequence(self, high_confidence_agents: Dict[str, float]) -> List[str]:
        """Generate optimal workflow sequence for recommended agents"""
        # Define workflow phases
        workflow_phases = {
            'initialization': ['project-owner', 'business-analyst', 'session-manager'],
            'architecture': ['enterprise-architect', 'software-architect', 'security-engineer'],
            'development': ['frontend-engineer', 'backend-engineer', 'api-engineer', 'data-engineer'],
            'quality': ['qa-engineer', 'security-engineer'],
            'deployment': ['deployment-engineer', 'platform-engineer', 'sre-engineer']
        }

        workflow_sequence = []
        for phase, phase_agents in workflow_phases.items():
            phase_recommendations = [agent for agent in phase_agents if agent in high_confidence_agents]
            workflow_sequence.extend(phase_recommendations)

        return workflow_sequence

    def _calculate_ensemble_performance(self, model_predictions: Dict[str, Dict[str, float]]) -> Dict[str, float]:
        """Calculate performance metrics for ensemble"""
        performance = {
            'model_agreement': self._calculate_model_agreement(model_predictions),
            'prediction_confidence': self._calculate_average_confidence(model_predictions),
            'model_coverage': len(model_predictions) / len(self.models)
        }

        return performance

    def _calculate_model_agreement(self, model_predictions: Dict[str, Dict[str, float]]) -> float:
        """Calculate agreement between models"""
        if len(model_predictions) < 2:
            return 1.0

        all_agents = set()
        for predictions in model_predictions.values():
            all_agents.update(predictions.keys())

        agreement_scores = []
        for agent in all_agents:
            agent_scores = []
            for predictions in model_predictions.values():
                if agent in predictions:
                    agent_scores.append(predictions[agent])

            if len(agent_scores) > 1:
                # Calculate variance (lower variance = higher agreement)
                mean_score = sum(agent_scores) / len(agent_scores)
                variance = sum((score - mean_score) ** 2 for score in agent_scores) / len(agent_scores)
                agreement = 1.0 / (1.0 + variance)  # Convert to agreement score
                agreement_scores.append(agreement)

        return sum(agreement_scores) / len(agreement_scores) if agreement_scores else 1.0

    def _calculate_average_confidence(self, model_predictions: Dict[str, Dict[str, float]]) -> float:
        """Calculate average prediction confidence"""
        all_scores = []
        for predictions in model_predictions.values():
            all_scores.extend(predictions.values())

        return sum(all_scores) / len(all_scores) if all_scores else 0.0

    def _generate_explanation(self, ensemble_scores: Dict[str, float],
                            model_predictions: Dict[str, Dict[str, float]]) -> str:
        """Generate human-readable explanation of recommendations"""
        top_agents = sorted(ensemble_scores.items(), key=lambda x: x[1], reverse=True)[:5]

        explanation = f"Based on ensemble analysis of {len(self.models)} models, "
        explanation += f"the top recommended agents are: "
        explanation += ", ".join([f"{agent} ({score:.2f})" for agent, score in top_agents])
        explanation += ". "

        # Add model agreement info
        model_agreement = self._calculate_model_agreement(model_predictions)
        if model_agreement > 0.8:
            explanation += "Models show high agreement on recommendations."
        elif model_agreement > 0.6:
            explanation += "Models show moderate agreement on recommendations."
        else:
            explanation += "Models show varied opinions, consider multiple options."

        return explanation

    def save_ensemble(self, filepath: str):
        """Save trained ensemble to file"""
        if not self.is_trained:
            raise ValueError("Cannot save untrained ensemble")

        ensemble_data = {
            'models': {},
            'model_weights': self.model_weights,
            'performance_metrics': self.performance_metrics,
            'is_trained': self.is_trained
        }

        # Save each model (simplified - in real implementation would use proper serialization)
        for name, model in self.models.items():
            ensemble_data['models'][name] = {
                'type': type(model).__name__,
                'is_trained': model.is_trained,
                'agent_names': getattr(model, 'agent_names', [])
            }

        with open(filepath, 'w') as f:
            json.dump(ensemble_data, f, indent=2)

        logger.info(f"Ensemble saved to {filepath}")

    def get_ensemble_summary(self) -> Dict[str, Any]:
        """Get summary of ensemble configuration and performance"""
        summary = {
            'models': list(self.models.keys()),
            'model_weights': self.model_weights,
            'is_trained': self.is_trained,
            'performance_metrics': self.performance_metrics
        }

        if self.is_trained:
            # Add model-specific info
            model_info = {}
            for name, model in self.models.items():
                model_info[name] = {
                    'type': type(model).__name__,
                    'agent_count': len(getattr(model, 'agent_names', [])),
                    'feature_importance_available': bool(getattr(model, 'feature_importance', {}))
                }
            summary['model_details'] = model_info

        return summary

def create_default_ensemble() -> EnsembleAgentRecommender:
    """Create default ensemble with standard models"""
    ensemble = EnsembleAgentRecommender()

    # Add models
    ensemble.add_model('random_forest', SimplifiedRandomForest(n_trees=10, max_depth=5))
    ensemble.add_model('neural_network', SimplifiedNeuralNetwork(hidden_layers=[64, 32]))
    ensemble.add_model('rule_based', RuleBasedValidator())

    return ensemble

def main():
    """Demo ensemble ML models"""
    print("🤖 AI-POWERED AGENT SELECTION - ENSEMBLE ML MODELS DEMO")
    print("=" * 80)

    # Create sample training data
    sample_training_data = TrainingData(
        project_features=[
            [0.8, 0.6, 0.3, 0.9, 0.4, 0.7, 0.2, 0.8] + [0.5] * 40,  # React + Python project
            [0.2, 0.9, 0.8, 0.3, 0.6, 0.4, 0.9, 0.1] + [0.3] * 40,  # Java enterprise project
            [0.6, 0.3, 0.9, 0.7, 0.2, 0.8, 0.5, 0.6] + [0.4] * 40,  # Data science project
        ],
        agent_selections=[
            ['frontend-engineer', 'backend-engineer', 'api-engineer', 'project-owner'],
            ['backend-engineer', 'enterprise-architect', 'security-engineer', 'project-owner'],
            ['data-engineer', 'data-scientist', 'backend-engineer', 'project-owner']
        ],
        success_metrics=[0.9, 0.8, 0.85],
        metadata=[
            {'project_type': 'web_app'},
            {'project_type': 'enterprise_system'},
            {'project_type': 'data_platform'}
        ]
    )

    # Create and train ensemble
    print("🔄 Creating ensemble with Random Forest, Neural Network, and Rule-based models...")
    ensemble = create_default_ensemble()

    print("🔄 Training ensemble on sample data...")
    ensemble.train(sample_training_data)

    # Test prediction
    test_features = [0.7, 0.5, 0.4, 0.8, 0.3, 0.6, 0.2, 0.7] + [0.4] * 40

    print("🔄 Generating recommendations for test project...")
    recommendations = ensemble.recommend_agents(test_features, confidence_threshold=0.5)

    # Display results
    print(f"\n🎯 AGENT RECOMMENDATIONS")
    print("=" * 80)

    print(f"📊 Model Performance:")
    for metric, value in recommendations.model_performance.items():
        print(f"  {metric}: {value:.3f}")

    print(f"\n🤖 Top Agent Recommendations:")
    print("-" * 40)
    for i, rec in enumerate(recommendations.primary_recommendations[:5], 1):
        confidence_level = "🟢" if rec.confidence_score > 0.7 else "🟡" if rec.confidence_score > 0.5 else "🔴"
        print(f"{i}. {rec.agent_name} {confidence_level}")
        print(f"   Confidence: {rec.confidence_score:.3f}")
        print(f"   Reasoning: {rec.reasoning[0] if rec.reasoning else 'Standard recommendation'}")
        if rec.alternative_agents:
            print(f"   Alternatives: {', '.join(rec.alternative_agents[:2])}")
        print()

    print(f"⚡ Recommended Workflow Sequence:")
    print("-" * 40)
    workflow_phases = []
    current_phase = []
    phase_agents = {
        'project-owner': 'Init', 'session-manager': 'Init',
        'frontend-engineer': 'Dev', 'backend-engineer': 'Dev', 'api-engineer': 'Dev',
        'qa-engineer': 'Test', 'security-engineer': 'Sec',
        'deployment-engineer': 'Deploy'
    }

    for agent in recommendations.workflow_sequence[:8]:  # Show first 8
        phase = phase_agents.get(agent, 'Other')
        print(f"  {phase}: {agent}")

    print(f"\n💡 Explanation:")
    print("-" * 40)
    print(f"  {recommendations.explanation}")

    # Show ensemble summary
    print(f"\n📋 ENSEMBLE SUMMARY:")
    print("-" * 40)
    summary = ensemble.get_ensemble_summary()
    print(f"  Models: {', '.join(summary['models'])}")
    print(f"  Model Weights: {summary['model_weights']}")
    print(f"  Training Status: {'✅ Trained' if summary['is_trained'] else '❌ Not Trained'}")

    print(f"\n✅ Ensemble ML models demonstrated successfully!")
    print("🚀 Ready for framework integration phase!")

if __name__ == "__main__":
    main()