# BlackJack

# Table of content

## Set up

---

### Installation

0. clone project

```bash
    git clone https://github.com/Xeei/final-project-compro2.git
    cd final-project-compro2
```

1. activate .venv

    - window (cmd not shell!!!)

        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```

    - macOS/Linux (terminal)

        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

2. set up env
    ```bash
    python -m pip install -r requirements.txt
    ```

### Start game

1. command

    - window

        ```bash
        python src/main.py
        ```

    - macOS/Linux
        ```bash
        python3 src/main.py
        ```

## How to play game

---

### word you should know

-   `hit` deal a card
-   `stand` confirm hand
-   `bust` score over **_21_**
-   `tie` player score and dealer score are the same (draw)

### Step to play the game

1. Menu Page - click on `Start Game` button to start the game
   <image src="./screenshots/gameplay/start_menu.png">
2. Player phase

    - `H` for hit a card (deal a card)
    - `S` for stand (confirm hand)
      <image src="./screenshots/gameplay/ingame.png">

3. Dealer phase
    - dealer will deal a card until score over `17`
4. End phase
    - if dealer is `bust` player will win
    - if player is `bust` player will lost immediately
    - if player score are the same as dealer will `tie`
    - if player score are `more than dealer` and `not over 21` player will win
    - `R` press `R` for restart
    - `Q` for quit game
      <image src="./screenshots/gameplay/result_page.png">

## Credits

---

-   [Table image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dblackjack%2Btable&psig=AOvVaw3NmQXaf6A61yrQhfg-qk3d&ust=1744205033203000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLiBo6zEyIwDFQAAAAAdAAAAABAn)

-   [52 Cards Images](https://acbl.mybigcommerce.com/52-playing-cards/)
