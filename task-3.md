
# Mastering Git and GitHub: A Step-by-Step Guide for Beginners  
(link for google docs: [Docs](https://docs.google.com/document/d/1fIOPxG2oayxLDc2CusvOJ2YGP7R6LkLvmVnpPVi2Xno/edit?usp=sharing))

Git and GitHub are two tools that almost everyone in **coding** and **research** has to come across at some point.  
The blog I’m reviewing does a solid job of explaining these basics in a *beginner-friendly* way.  

In this review, I’ll go through what really worked for me as a learner and also share a few things I would have found helpful if I were a first-timer.  


## 🔹 Git vs GitHub  

The blog starts off by explaining **Git** as a *Version Control System* that helps track code over time as it stores *snapshots* (commits) of your code, which you can revert to any time, irrespective of a language/framework.  

I liked how the author described its **distributed** nature, since you can collaborate without being on the same network by *pushing* your code to remote storage in **GitHub**, which is described as a *cloud-based platform* that save and keep projects accessible from anywhere.  

👉 This framing finally helped me see the connection between the two. I've seen Git vs GitHub debates online before, now it finally clicked to me why people confuse them, and how they're literally so different.


## 🔹 First Setup  

The author lays out a step-by-step guide to installing Git and setting up configs:  


git config --global user.name "[f_name l_name]"   # author identity setup
git config --global user.email "[email]"          # email setup for commits
git config --global color.ui auto                 # gives colored output in terminal

--global → applies the setting across all repositories for that user.

Repositories → store code systematically (like a container).

## 🔹 Basic Workflow

The blog also walks through the basic workflow: you start by running *git init* to initialize a new repository in your current directory. On GitHub, you create a repo (with a name and README), then link it to your local one using *git remote add origin <link>*.

After that, the flow becomes:
1. stage files with git add .
2. take a snapshot with git commit -m "msg"
3. upload it to GitHub using git push origin master

The author also explains the .gitignore file, which tells Git to skip bulky folders (node_modules), sensitive files (*.db or *.sqlite), and unnecessary build/log files.

## 🔹 Advanced Topics

The later sections are where things got serious. Logs, resets, reverts, branching, and collaboration with forks and pull requests. The explanations were good, but honestly, a true beginner with no prior exposure might struggle a bit.

There is a lot of jargon (commits, branches, aliases, staging etc), while the author does explain them, it can still feel overwhelming if you don’t already know a little bit of Git.

That said, for someone like me who has some prior experience, it really helped fill knowledge gaps and connect concepts I didn’t understand earlier.

## 🔹 Open Source

Lastly, the author concludes the blog by introducing ‘Open Source’ (a software whose code is public and freely available to use, modify, and share).

Popular events like Google Summer of Code (GSoC) and Hacktoberfest give learners a chance to contribute, open internship opportunities, expand network, and grow overall.

## 🔹 Final Thoughts

Overall, this blog helped me understand Git and GitHub much better and gave me a clearer picture of open source. It also made me curious to explore open source projects myself, as this blog mentions, it is the next step after learning the basics.