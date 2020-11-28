# Luluchess

Creating a chess game without any built-in functions with Python.

## Tests

To run tests, make `python API/test.py`.

## Structure

`Piece` objects have this structure
```json
{
    "type": "K",
    "color": "white",
    "square": "f3"
}
```
`type` can be `K` (Knight), `B` (Bishop), `P` (Pawn), `K` (King), `Q` (Queen) or `R` (Rook).

`color` can be `white` or `black`.


`Move` objects have this structure
```json
{
    "start": "g2",
    "end": "g4"
}
```

`Board` objects have this structure
```json
{
    "a1": Piece,
    "a2": Piece,
    ...
    "h8": Piece
}
```

`Game` objects have this structure
```json
{
    "0": Board,
    "1": Board,
    ...
}
```

