@echo off

cd %~dp0
py -m pip install --upgrade pip setuptools wheel
py -m pip install pygame
py -m pip install --upgrade pygame
python game.py
