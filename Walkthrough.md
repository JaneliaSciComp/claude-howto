# Janelia Claude-a-thon Walkthrough

This is a hands-on hacking session for new users of Claude Code to build familiarity with its capabilities. 

## Agenda

* Set up your Anthropic account
* Install Claude Code on your laptop
* Guided walkthroughs of common real-life scenarios:
    * Fix a bug in an existing project
    * Get help with understanding an existing project
    * Generate a new project from scratch

During the session we will touch on basic features of Claude Code including permissions, context management, and model usage.

Please note that this workshop focuses on hands-on setup and foundational skills. It is not a deep dive into advanced workflows or an open discussion session. For those looking for more, Erick Matsen’s [recorded session](https://hhmi.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=82a4d9aa-3c64-4a48-8de0-b38000f7bdaa) is highly recommended.

## Create a Claude account

If you don't have a Claude subscription, navigate to [https://claude.ai/upgrade](https://claude.ai/upgrade) and login with your Google Workspace account. 

Sign up for the "Pro" subscription, billed monthly.

> [!IMPORTANT]
> Make sure to disable the "Help improve Claude" setting found under Settings → Privacy.
>
> <img width="600" src="https://github.com/user-attachments/assets/1d88bd0e-c04d-4011-a451-351c74bae73c" />

## Installation and Setup

### 1) Install Claude Code

You can use this command to install [Claude Code](https://code.claude.com/docs/en/setup) on your laptop:
```
curl -fsSL https://claude.ai/install.sh | bash
```
Make sure to follow the installer's advice about adding the path to your `.bashrc` file.

### 2) Start Claude Code

Now create a folder that you can use for this hackathon and run Claude Code inside of it:
```
mkdir claude-a-thon
cd claude-a-thon
claude
```
Accept the default look and feel.

### 3) Login 

Continue following the prompts (😉) to login using "Claude account with subscription" and follow the browser auth flow to authorize Claude Code. It is safe to accept the default settings.

## Exercise 1: Bug Fixing

Paste this into prompt into Claude Code:
```
Clone this project and get it running: https://github.com/google/neuroglancer
Then add a button to the top right (to the right of Edit JSON State) which
copies the current URL to the clipboard.
```

### Permissions

As Claude Code works through the problem it will prompt you for any action it needs to take. Be careful with allowing items with "Don't ask again"! It's better to run Claude Code in a sandbox before giving it free priviledges (more on this later).

You can use the `/permissions` command to read/modify your permission scheme. Alternatively, edit `.claude/settings.local.json` either in your project or in your home directory. This will require restarting Claude Code however.

### Planning Mode

You can switch to plan mode using shift-tab and try the prompt again. This time, Claude takes it's time to analyze the problem and come up with a better solution.

### The Solution

Claude can easily find the place to make the change, and write correct code for it every time. Unfortunately, the default implementation it creates is not ideal. As Neuroglancer users know, the URL can sometimes become too long to be copied from the URL address bar, and the naive implementation fails the same way. This kind of context is something you would need to provide. What's more, is you will most likely need to tell it exactly *how* to solve the problem ("serialize the Neuroglancer state and copy that to the clipboard").

## Exercise 2: Code Analysis

When starting work on a new problem, always use a fresh context. This can be accomplished with the `/clear` command. It's important to manage your context over time. You may hit token limits, and the model may suffer context collapse even before that happens. Context collapse means that the model will not be able to use all of the information in them model. Use `/context` to interrogate the current state of the context. You can use `/compact` to summarize the current context into fewer tokens.

After clearing the context, execute this prompt:
```
Clone and analyze the project at https://github.com/JaneliaSciComp/BigStitcher
and produce a Markdown file that summarizes the structure and how this project
should be developed.
```

Feel free to replace the URL with another project. Claude Code is very useful for understanding projects that you are getting started with. It's also great for writing/updating documentation after changes are made.

### Thinking

There are some bugs with the [thinking settings](https://github.com/anthropics/claude-code/issues/10623) in the latest versions of Claude Code. The latest version is always thinking. To disable it, set `MAX_THINKING_TOKENS=0` in the shell environment:
```
MAX_THINKING_TOKENS=0 claude
```

## Exercise 3: Rapid Prototyping

Let's first configure a sandbox so that we can give Claude Code a little more freedom to act. Use the `/sandbox` command to enable it (you can use the defaults). 

Now paste in this prompt to one-shot a prototype:

```
Create a Pixi Python project and use the zarr library to open this dataset:
s3://janelia-cosem-datasets/jrc_mus-hippocampus-3/jrc_mus-hippocampus-3.zarr
Create a CLI that will let me extract a random 1024x1024xN crop (configurable
number of z slices) and encode the frames into an h264 movie.
```

You are now "vibe coding"!




