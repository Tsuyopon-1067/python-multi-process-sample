#!/bin/bash
#
function help () {
    echo "help"
    echo "create"
    echo "  python3 -m venv .venv"
    echo "  . .venv/bin/activate"
    echo "start"
    echo "  . .venv/bin/activate"
    echo "end"
    echo "  deactivate"
}

function create () {
    # Create virtual environment
    python3 -m venv .venv
    start
}

function start() {
    # Activate
    . .venv/bin/activate
}

function end () {
    deactivate
}

if [ $# -eq 1 ]; then
    case $1 in
        "h" | "help") help ;;
        "c" | "create") create ;;
        "s" | "start") start ;;
        "e" | "end") end ;;
        *) help ;;
    esac
else
    help
fi

