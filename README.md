# Authors - Boris Matenco, Oskar Smaga
# Tic Tac Toe AI — Reinforcement Learning

Projekt wykorzystuje Q-Learning oraz Reinforcement Learning do nauki gry Tic Tac Toe 4x4 poprzez self-play training.

## Cechy
- Q-Learning
- Reinforcement Learning
- Self-play AI training
- Persistent AI memory (Q-Table)
- AI vs AI simulation
- Tkinter GUI
- 4x4 board

## Jak działa?

Dwa modele AI grają przeciwko sobie tysiące partii.

Po każdej grze aktualizowane są wartości Q dla wykonanych ruchów.

AI uczy się:
- blokowania przeciwnika,
- budowania linii,
- optymalnej strategii.

Po treningu większość gier kończy się remisem, co oznacza osiągnięcie optymalnej gry.