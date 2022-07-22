#!/usr/bin/env bash
set -Ceu
#---------------------------------------------------------------------------
# seleniumとchrome-driverをインストールする。
# ラズパイ4におけるインストール手順。
# CreatedAt: 2022-07-22
#---------------------------------------------------------------------------
Run() {
	THIS="$(realpath "${BASH_SOURCE:-0}")"; HERE="$(dirname "$THIS")"; PARENT="$(dirname "$HERE")"; THIS_NAME="$(basename "$THIS")"; APP_ROOT="$PARENT";
	cd "$HERE"
	sudo pip3 install selenium
	sudo apt-get install chromium-chromedriver
	which chromedriver
	chromedriver --version
	python3.7 run.py
}
Run "$@"
