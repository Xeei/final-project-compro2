# Blackjack Project

## 1. Project Overview

**Blackjack** is a game where the goal is to make the total score of the cards in your hand as close as possible to 21—without going over. If the total goes over 21, it is called a **"bust"**, and the player loses the round.

## 2. Project Review

This version of Blackjack introduces **special skills/cards** that help the player win more easily. These special cards add strategic depth and variation to the traditional rules.

## 3. Programming Development

### 3.1 Game Concept

-   The game uses a standard deck of **52 cards**.
-   At the start of each round:
    -   The **player receives 2 cards**.
    -   The **dealer receives 2 cards**, but **only one is visible** to the player.
-   The player can:
    -   **Draw more cards** to improve their score.
    -   **Use special cards** with unique effects.
-   If the player's score exceeds 21, they **bust** and lose the round.
-   If the player doesn't bust, their score is **compared to the dealer’s**.
    -   The score **closest to 21 wins**.

### 3.2 Object-Oriented Programming Implementation

The game is designed using **Object-Oriented Programming (OOP)**. A UML diagram is created in Lucidchart to visualize the structure.
<image src="./document/UML.png"/>
**Main Classes:**

-   `Card`: Represents a playing card with suit and value.
-   `Deck`: Handles deck creation, shuffling, and drawing cards.
-   `Player`: Tracks player's hand, score, and actions.
-   `Dealer`: Inherits from Player but follows different rules for drawing.
-   `GameUI`: Handle events in game.
-   `GameDb`: Manages data and store data.
-   `App`: Combine game and visualization program.

### 3.3 Algorithms Involved

-   **Linear Search**: Used when a special card is activated to find a specific card from the deck.
-   **Sorting Algorithm**: Used to sort player history (e.g. by score or time).
-   **Game Logic**: Decision trees and conditional branches control when and how players can act.

## 4. Statistical Data (Prop Stats)

### 4.1 Data Features

The game will collect the following data each round:

-   Number of cards played by the player.
-   Total score of the player each round.
-   Win/Loss outcome.
-   Time taken for each decision made by the player.

## Feature Data Collection and Usage

| **Feature**                         | **Why is it Useful?**                                                  | **How to Obtain 50 Values?**                                               | **Variable & Class**                                               | **Display Method**                                                 |
| ----------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| **Cards Player Has Each Round**     | Helps analyze why the player chose to hit or stand with certain cards. | Log each round into SQLite when the player plays.                          | `self.__cards` from class `Player`                                 | Show percentage of hit/stand choices per card (Bar chart or Table) |
| **Score of Player Hand Each Round** | Reveals the most common scores and helps understand win/loss trends.   | Extract score each round from game history.                                | `self.score` from class `Entity`                                   | Table showing score vs win/loss outcome                            |
| **Win/Lose Rate**                   | Measures how well the player performs overall.                         | Count total wins and losses across games in the database.                  | Derived from game result logs                                      | Pie chart or percentage display                                    |
| **Player Bet**                      | Shows how the player gains or loses money through betting.             | Retrieve bet each round from game log.                                     | `self.bet` from class `GameUI`                                     | Show total gain/loss, possibly with a line graph or summary table  |
| **Time Used per Decision**          | Analyzes how much time the player takes to make decisions.             | Log timestamps for each hit/stand decision and calculate time differences. | `self.start_time` and `self.player_time_stamp` from class `GameUI` | Scatter plot showing score vs decision time                        |

## Feature Data Visualization Plan

| **Graph/Table Name** | **Feature Name**                | **Graph Objective**                                         | **Graph Type**                 | **X-Axis** | **Y-Axis**                |
| -------------------- | ------------------------------- | ----------------------------------------------------------- | ------------------------------ | ---------- | ------------------------- |
| **Graph1**           | Score of Player Hand Each Round | Show history of player scores in past games                 | Histogram                      | Score      | Frequency                 |
| **Graph2**           | Win/Lose Rate                   | Show percentage of wins and losses                          | Pie Chart                      | -          | Win/Lose over total games |
| **Graph3**           | Time Used per Decision          | Show how long player takes to make decisions based on score | Scatter Plot (Hue = Hit/Stand) | Score      | Time Used                 |
| **Table**            | Cards Player Has Each Round     | Show detailed data of player’s cards each round             | Table                          | -          | -                         |

### Frequecy of score

<image src="./screenshots/visualization/histogram.png"/>

### Porpotion of WIN/LOST/TIE

<image src="./screenshots/visualization/piechart.png"/>

### Pair between score and decision time use

<image src="./screenshots/visualization/pair.png"/>

### Data table

<image src="./screenshots/visualization/table.png"/>

## 4.2 Data Recording Method

Record data in sql(sqlite) game will store data of how many player had play. How many time win/lose. and what score that he win with.

## 4.3 Data Analysis Report

win rate base on number of card and win rate base on score

## 5. Project Timeline

| **Week** | **Date** | **Task**                                 |
| -------- | -------- | ---------------------------------------- |
| Week 1   | 10 March | Proposal submission / Project initiation |
| Week 2   | 17 March | Full proposal submission                 |
| Week 3   | 24 March | Game process                             |
| Week 4   | 31 March | Game UI                                  |
| Week 5   | 7 April  | Report UI                                |
| Week 6   | 14 April | Submission week (Draft)                  |

## 6. Video Presentation

-   [youtube link](https://youtu.be/4vk-7XwjIeE)
