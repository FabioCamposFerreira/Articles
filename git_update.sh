#!/bin/sh

# ----------------------------------
# Colors
# ----------------------------------
NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'

echo "Updating Articles repository"
cd "/run/media/fab/Novo volume/FCF/Projects/Articles/"
git pull && echo -e "${GREEN}OK git pull${NOCOLOR}" || exit 1
git add . && echo -e "${GREEN}OK git add${NOCOLOR}" || exit 1
git commit -m 'Sem comentarios' && echo -e "${GREEN}OK git commit${NOCOLOR}" || exit 1
git push -u origin main && echo -e "${GREEN}OK git push${NOCOLOR}" || exit 1
echo -e "${GREEN}updated repository Articles${NOCOLOR}"