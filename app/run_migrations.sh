#!/bin/bash

piccolo migrations new db --auto

piccolo migrations forwards all