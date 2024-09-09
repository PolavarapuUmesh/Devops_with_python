import os
import subprocess

def automate_build():
    subprocess.run(['git', 'clone', 'https://github.com/PolavarapuUmesh/hangman-game.git'])
    subprocess.run(['mvn', 'clean', 'package'])
    subprocess.run(['docker', 'build', '-t', 'your_image_name'])
    subprocess.run(['docker', 'run', '-d', '-p', '8081:8081', 'your_image_name'])

if __name__ == '__main__':
    automate_build()