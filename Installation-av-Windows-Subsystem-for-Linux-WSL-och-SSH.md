
# Steg-för-steg Guide för WSL och GitHub

## 1. Installera WSL och Ubuntu

1. Öppna PowerShell som administratör och kör:
```bash
wsl --install -d ubuntu
```

2. Starta om din dator. Efter omstarten kommer du se:
```
Ubuntu is already installed.
Launching Ubuntu...
Installing, this may take a few minutes...
Please create a default UNIX user account.
Enter new UNIX username: "ditt_användarnamn"
New password: "********"
Retype new password: "********"
passwd: password updated successfully
Installation successful!
```

## 2. Grundkonfiguration

1. Uppdatera paketlistan:
```bash
sudo apt update
```
Förväntad utskrift:
```
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
...
```

2. Installera nödvändiga verktyg:
```bash
sudo apt install python3-pip pwgen openssh-server git -y
```

## 3. SSH-nyckelkonfiguration

1. Skapa SSH-nyckelpar:
```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/netudy
```
Du kommer att se:
```
Generating public/private rsa key pair.
Enter passphrase: "ditt_säkra_lösenord"
Enter same passphrase again: "ditt_säkra_lösenord"
Your identification has been saved in /home/dittanvändarnamn/.ssh/netudy
Your public key has been saved in /home/dittanvändarnamn/.ssh/netudy.pub
The key fingerprint is:
SHA256:... dittanvändarnamn@dittdatornamn
The key's randomart image is:
[ASCII-konstverk visas här]
```

2. Starta SSH-tjänsten:
```bash
sudo service ssh start
sudo ufw allow ssh
```

## 4. GitHub-inställningar

1. Visa din publika nyckel:
```bash
cat ~/.ssh/netudy.pub
```
Kopiera hela utskriften som ser ut ungefär så här:
```
ssh-rsa AAAAB3...långnyckel...== dittanvändarnamn@dittdatornamn
```

2. Gå till GitHub > Settings > SSH and GPG keys > New SSH key
   - Titel: "WSL Nyckel"
   - Klistra in din publika nyckel
   - Klicka på "Add SSH key"

## 5. Klona Projektet

1. Skapa och gå till src-katalog:
```bash
mkdir -p ~/src && cd ~/src
```

2. Klona repot:
```bash
git clone git@github.com:netudy/ubuntu-school.git
```
Första gången kommer du se:
```
The authenticity of host 'github.com (140.82.121.3)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Enter passphrase for key '/home/dittanvändarnamn/.ssh/netudy':
[Kloning fortsätter...]
```

## 6. Skapa och Pusha Din Första Commit

1. Gå till projektkatalogen:
```bash
cd ubuntu-school
```

2. Skapa en ny gren:
```bash
git checkout -b "dittnamn-first-commit"
```

3. Skapa din fil:
```bash
cat <<"EOF" > dittnamn.2024.08.23.sh
#!/bin/sh
echo "Min första skriptfil"
exit 0
EOF
```

4. Lägg till filen:
```bash
git add dittnamn.2024.08.23.sh
```

5. Konfigurera git (gör bara en gång):
```bash
git config --global user.name "Ditt Namn"
git config --global user.email "din.email@example.com"
```

6. Skapa commit:
```bash
git commit -m "Min första commit"
```
Förväntad utskrift:
```
[dittnamn-first-commit bb4cd6f] Min första commit
 1 file changed, 3 insertions(+)
 create mode 100644 dittnamn.2024.08.23.sh
```

7. Pusha till GitHub:
```bash
git push --set-upstream origin dittnamn-first-commit
```
Du kommer se:
```
Enumerating objects: 4, done.
...
To github.com:netudy/ubuntu-school.git
 * [new branch]      dittnamn-first-commit -> dittnamn-first-commit
Branch 'dittnamn-first-commit' set up to track remote branch 'dittnamn-first-commit' from 'origin'.
```

## 7. Verifiera på GitHub

1. Öppna din webbläsare och gå till:
```
https://github.com/netudy/ubuntu-school/tree/dittnamn-first-commit
```
2. Kontrollera att din fil syns med dina ändringar.

Grattis! Du har nu:
- Skapat en WSL-miljö
- Konfigurerat SSH-nycklar
- Kopplat till GitHub
- Skapat din första commit och push
```
