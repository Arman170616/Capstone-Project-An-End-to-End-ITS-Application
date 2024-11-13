import numpy as np
import random

class QLearningTrafficOptimization:
    def __init__(self, n_actions=4, n_states=3, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.995, min_exploration_rate=0.01):
        self.n_actions = n_actions  # Number of possible actions (traffic light signals)
        self.n_states = n_states  # Number of possible states (traffic congestion levels)
        self.learning_rate = learning_rate  # Learning rate (alpha)
        self.discount_factor = discount_factor  # Discount factor (gamma)
        self.exploration_rate = exploration_rate  # Exploration rate (epsilon)
        self.exploration_decay = exploration_decay  # Decay factor for exploration rate
        self.min_exploration_rate = min_exploration_rate  # Minimum exploration rate

        # Q-table initialized to zero, where rows represent states and columns represent actions
        self.q_table = np.zeros((n_states, n_actions))

    def get_state(self, congestion_level):
        """Map congestion level to state"""
        return congestion_level  # Maps 0: low, 1: medium, 2: high

    def choose_action(self, state):
        """Choose action based on epsilon-greedy policy"""
        if random.uniform(0, 1) < self.exploration_rate:
            action = random.choice(range(self.n_actions))
        else:
            action = np.argmax(self.q_table[state])
        return action

    def update_q_table(self, state, action, reward, next_state):
        """Update the Q-table using the Q-learning formula"""
        best_next_action = np.argmax(self.q_table[next_state])
        old_q_value = self.q_table[state, action]
        new_q_value = old_q_value + self.learning_rate * (reward + self.discount_factor * self.q_table[next_state, best_next_action] - old_q_value)
        self.q_table[state, action] = new_q_value

    def decay_exploration_rate(self):
        """Decays the exploration rate over time"""
        if self.exploration_rate > self.min_exploration_rate:
            self.exploration_rate *= self.exploration_decay

    def simulate(self, traffic_data, max_steps=1000):
        """Simulate the optimization of traffic signals based on traffic data."""
        total_reward = 0
        for step in range(max_steps):
            congestion_level = traffic_data[step % len(traffic_data)]
            state = self.get_state(congestion_level)
            action = self.choose_action(state)
            reward = -abs(action - state)  # Custom reward function
            next_state = state
            self.update_q_table(state, action, reward, next_state)
            self.decay_exploration_rate()
            total_reward += reward

        print(f"Total reward after {max_steps} steps: {total_reward}")


# Example usage
if __name__ == "__main__":
    traffic_data = [0, 1, 2, 1, 0, 2, 1, 0, 1, 2]  # Sample traffic data (congestion levels)
    q_learning = QLearningTrafficOptimization()
    q_learning.simulate(traffic_data)
