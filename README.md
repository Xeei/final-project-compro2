# BlackJack

# Table of content

## Set up

---

### Installation

1. set up env
    ```bash
    pip install -r requirements.txt
    ```

### Start game

1. command
    ```bash
    python src/game_runner.py
    ```

## How to play game

---

### word you should know

-   `hit` deal a card
-   `stand` confirm hand
-   `bust` score over **_21_**
-   `tie` player score and dealer score are the same (draw)

### Step to play the game

1. Menu Page
    - click on play text to start the game
2. Player phase
    - `H` for hit a card (deal a card)
    - `S` for stand (confirm hand)
3. Dealer phase
    - dealer will deal a card until score over `17`
4. End phase
    - if dealer is `bust` player will win
    - if player is `bust` player will lost immediately
    - if player score are the same as dealer will `tie`
    - if player score are `more than dealer` and `not over 21` player will win
5. Choice
    - `R` press `R` for restart
    - `Q` for quit game

## Credits

---

-   [Table image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dblackjack%2Btable&psig=AOvVaw3NmQXaf6A61yrQhfg-qk3d&ust=1744205033203000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLiBo6zEyIwDFQAAAAAdAAAAABAn)

-   [52 Cards Images](https://acbl.mybigcommerce.com/52-playing-cards/)
