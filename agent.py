import numpy as np
import random



class Agent:
    def __init__(self, features, actions, learning_rate, discount_rate, epsilon):
        self.shape = tuple([2 for n in range(features)] + [actions])
        self.q_table = np.zeros(self.shape, dtype='float')
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.epsilon = epsilon
        self.possible_actions = actions
        self.p_state = None

    def get_action(self, state):
        self.p_state = state
        # Observe Current state s and locate it on table
        possible_actions = self.q_table[state[0]][state[1]][state[2]][state[3]][state[4]][state[5]][
            state[6]][state[7]][state[8]][state[9]][state[10]][state[11]]
        # select action a and execute it using epsilon greedy
        ep = random.random()
        if ep < self.epsilon:
            # choose random action
            action = random.randint(0, self.possible_actions - 1)
            return action
        else:
            # choose the action with highest q_value for the state
            return np.argmax(possible_actions)

    def updateQTable(self, state, action, reward, next_state):
        # implementation of the Q-Learning Algorithm
        possible_next_state_actions = self.q_table[next_state[0]][next_state[1]][next_state[2]][next_state[3]][next_state[4]][next_state[5]][
            next_state[6]][next_state[7]][next_state[8]][next_state[9]][next_state[10]][next_state[11]]
        current_Q_value = self.q_table[state[0]][state[1]][state[2]][state[3]][state[4]][state[5]][
            state[6]][state[7]][state[8]][state[9]][state[10]][state[11]][action]
        Q_value = current_Q_value + self.learning_rate * (reward + self.discount_rate * max(possible_next_state_actions) - current_Q_value)
        # Actual Update
        self.q_table[state[0]][state[1]][state[2]][state[3]][state[4]][state[5]][
            state[6]][state[7]][state[8]][state[9]][state[10]][state[11]][action] = Q_value
        return Q_value
    def endEpisode(self):
        self.epsilon *= 0.995