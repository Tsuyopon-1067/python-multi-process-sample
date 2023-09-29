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
}

if [ $# -eq 1 ]; then
    case $1 in
        "c" | "create") create ;;
        *) help ;;
    esac
else
    help
fi

