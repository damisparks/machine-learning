import numpy as np
from physics_sim import PhysicsSim
import math

class Defined_Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4

        # starting position 
        self.init_pose = init_pose if init_pose is not None else np.array([0.,0.,0.,0.,0.,0.])

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""
        reward = 0.0
        done = False

        # reward will be 0, if the target is matched or negative if it move farther away
        reward = -min(abs(self.target_pos[2] - self.init_pose[2]), 20.0) 

        if self.init_pose[2] >= self.target_pos[2]: # if target is  reached or passed 
            reward += 10.0 # 10 is given as a reward 
            done = True 
        elif self.sim.time > self.sim.runtime: # agent has run out of time 
            reward -= 10.0 # punishment for the agent 
            done = True
        return reward 
     
        # below are some references.
        #https://www.w3resource.com/python-exercises/python-basic-exercise-40.php 
        # https://www.wolframalpha.com/educators/lessonplans/Calculating_Distances_in_Two_and_Three_Dimensions.pdf


    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state
