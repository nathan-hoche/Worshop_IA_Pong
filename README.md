<h1 align="center">
    Workshop - AI Pong
</h1>

<p align="center">
    <img width="500" height="300" src="https://www.hiig.de/wp-content/uploads/2014/11/Pong-1200x800.jpg">
</p>
<br>

<h3 align="center">
    The goal of this workshop is to create your first artificial intelligence capable of winning at Pong every time.
</h3>
<br><br>

### **What's Pong?**

Pong is one of the first arcade video games and the first sports arcade video game.<br>
The game is inspired by table tennis in top view, and each player competes by moving the virtual racket up and down, via a rotary button, to keep the ball in the playing field. The player can change the direction of the ball depending on where the ball hits the racket, while its speed gradually increases during the round.<br><br>

### **What's an AI?**

Artificial Intelligence (AI) is "the set of theories and techniques used to create machines capable of simulating intelligence".<br> 
Often classified in the cognitive sciences group, it involves computational neurobiology (particularly neural networks), mathematical logic (part of mathematics and philosophy) and computer science. She is looking for methods to solve problems with high logical or algorithmic complexity.<br><br>

# **Initialization**

In a first time, you need to clone the workshop repo with:
```
git clone git@github.com:nathan-hoche/Worshop_IA_Pong.git
```

Now you can launch the game with:
```
python3 Pong.py
```

> You need tkinter module for this workshop.<br>
> If you don't have him, install him with:
```python
sudo apt-get install python3-tk
or
sudo dnf install python3-tkinter
```
<br><br>

# **Command**

You can use all this command to program the AI:

> All of this commands is present in user module.

* This function returns the position of your ball
```python
get_pos()
```
* This function returns the speed of your ball
```python
get_speed()
```
* This function returns the position of your bar
```python
get_bar_pos()
```
* This function moves the pong bar upwards.
```python
up_ia_bar()
```
* This function moves the pong bar down.
```python
down_ia_bar()
```

<br><br>

# **Objective**

The goal of the project is to code the artificial intelligence of a Pong game which must win every time and for that it is necessary to modify the "IA.py".<br>
Like this example:<br>

## **Exemple**

```python
from src.user import user

class launch_ia():
    def __init__(self):
        self.info = user()
        self.nb = 10
        return

    def program_IA(self):
        if (self.nb != 0):
            self.info.down_ia_bar()
            self.nb -= 1
            print(self.info.get_speed())
            print(self.info.get_pos())
        return
```
> Don't touch other file to programm the AI.

<br><br>


# **To go further**

Here are some examples to go further in the workshop:

* Continue the AI to beat all the players
* Complete and personalize the Pong
* Do a pong screensaver