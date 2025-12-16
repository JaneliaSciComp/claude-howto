# Janelia Claude-a-thon (Dec 16, 2025)

> [!IMPORTANT]
> This is a skeleton for use during live training. You can view the full [walkthrough](Walkthrough.md) for the complete details and commentary.

## Agenda

* Set up your Anthropic account
* Install Claude Code on your laptop
* Guided walkthroughs of common real-life scenarios:
    * Fix a bug in an existing project
    * Get help with understanding an existing project
    * Generate a new project from scratch

## Create a Claude account

If you don't have a Claude subscription, navigate to [https://claude.ai/upgrade](https://claude.ai/upgrade) and login with your Google Workspace account. Sign up for the "Pro" subscription, billed monthly.

## Installation and Setup

1) [Install Claude Code](https://code.claude.com/docs/en/setup) on your laptop:
```
curl -fsSL https://claude.ai/install.sh | bash
```

2) Create a folder that you can use for this hackathon and run Claude Code inside of it:
```
mkdir claude-a-thon
cd claude-a-thon
claude
```

3) Login using "Claude account with subscription" and follow the browser auth flow to authorize Claude Code. 

## Exercise 1: Bug Fixing

Paste this into prompt into Claude Code:
```
Clone this project and get it running: https://github.com/google/neuroglancer
Then add a button to the top right (to the right of Edit JSON State) which
copies the current URL to the clipboard.
```

Useful commands:
* `/permissions` - allow or deny Claude access to specific actions


## Exercise 2: Code Analysis

Clear the context with `/clear`, then paste in this prompt:
```
Clone and analyze the project at https://github.com/JaneliaSciComp/BigStitcher
and produce a Markdown file that summarizes the structure and how this project
should be developed.
```

Other useful commands:
* `/context` - show the current state of context usage
* `/compact` - summarize the current tokens to use fewer tokens


## Exercise 3: Rapid Prototyping

Use `/sandbox` to configure a safe execution environment.

Then paste in this prompt:
```
Create a Pixi Python project and use the zarr library to open this dataset:
s3://janelia-cosem-datasets/jrc_mus-hippocampus-3/jrc_mus-hippocampus-3.zarr
Create a CLI that will let me extract a random 1024x1024xN crop (configurable
number of z slices) and encode the frames into an h264 movie.
```

