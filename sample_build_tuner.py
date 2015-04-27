#!/usr/bin/env python
#
# Optimize blocksize of apps/mmm_block.cpp
#
# This is an extremely simplified version meant only for tutorials
#
import adddeps  # fix sys.path

import argparse

import opentuner
from opentuner import ConfigurationManipulator
from opentuner import IntegerParameter
from opentuner import MeasurementInterface
from opentuner import Result

import skill_list

class TestTuner(MeasurementInterface):

  def manipulator(self):
    """
    Define the search space by creating a
    ConfigurationManipulator
    """
    print self.args.level

    manipulator = ConfigurationManipulator()

    skill_list.add_skills(manipulator)
    
    return manipulator

  def run(self, desired_result, input, limit):
    """
    Mess around with stuff, try to figure it out
    """
    cfg = desired_result.configuration.data

#   Should return 0 if OK. Returns a higher number the more invalid the setup is.
#   For example, 4 if it has 4 unsatisfied requirements, and 7 if it has 7 unsatisfied
#   requirements.
    valid_status = skill_list.check_validity(cfg)
    
    if valid_status != 0:
      return Result(time = valid_status)

    res = skill_list.calc_results(cfg)
    
    return Result(time = -total_dmg) 

  def save_final_config(self, configuration):
    """called at the end of tuning"""
    print "Optimal block size written to test_final_config.json:", configuration.data
    self.manipulator().save_to_file(configuration.data,
                                    'test_final_config.json')


if __name__ == '__main__':
  argparser = opentuner.default_argparser()

  #TODO: Ver se isso fica aqui
  argparser.add_argument('--level', type=int, default=5,
                         help='Level to optimze')
  #TODO: Generate
  TestTuner.main(argparser.parse_args())
