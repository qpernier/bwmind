import { Constant } from '../constant';

export class Pawn{
    public top:string;
    public left:string;
    public img: string = 'assets/pawn/black_king.png';

    constructor(public id:number,public owner:string, public fk_game_id: number, public code: string, public vertical_coord: number, public horizontal_coord:number){
        this.top = (((7 - this.vertical_coord) * Constant.squareSize) + 20) + 'px';
        this.left = ((this.horizontal_coord * Constant.squareSize) + 20) + 'px';
        if (owner === "player1" && code === "king") {
            this.img = 'assets/pawn/white_king.png';
        } else if (owner === "player1" && code === "queen") {
            this.img = 'assets/pawn/white_queen.png';
        } else if (owner === "player1" && code === "bishop") {
            this.img = 'assets/pawn/white_bishop.png';
        } else if (owner === "player1" && code === "knight") {
            this.img = 'assets/pawn/white_knight.png';
        } else if (owner === "player1" && code === "rook") {
            this.img = 'assets/pawn/white_rook.png';
        } else if (owner === "player1" && code === "pawn") {
            this.img = 'assets/pawn/white_pawn.png';
        } else if (owner === "player2" && code === "king") {
            this.img = 'assets/pawn/black_king.png';
        } else if (owner === "player2" && code === "queen") {
            this.img = 'assets/pawn/black_queen.png';
        } else if (owner === "player2" && code === "bishop") {
            this.img = 'assets/pawn/black_bishop.png';
        } else if (owner === "player2" && code === "knight") {
            this.img = 'assets/pawn/black_knight.png';
        } else if (owner === "player2" && code === "rook") {
            this.img = 'assets/pawn/black_rook.png';
        } else if (owner === "player2" && code === "pawn") {
            this.img = 'assets/pawn/black_pawn.png';
        }
    }
}