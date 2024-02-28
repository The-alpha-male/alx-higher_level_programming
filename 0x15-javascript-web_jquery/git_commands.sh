#!/bin/bash

# Ask user for commit message
echo "Enter commit message:"
read commit_message

# Add all changes
git add .

# Commit changes with custom message
git commit -m "$commit_message"

# Push changes
git push

