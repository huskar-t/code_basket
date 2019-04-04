# coding: utf-8
import os
root = os.path.dirname(__file__)
log_dir = os.path.join(root, "log")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)