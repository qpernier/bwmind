import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Square } from '../models/square';
import { GameService } from './game.service';
import { Pawn } from '../models/pawn';
import { Urls, Constant } from '../constant';
import { Coord } from '../models/coord';
import _ from "lodash";

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {
  /**Id of the current game */
  gameId: number = null;

  /** Code of the playing IA */
  iaCode: string = null;

  /** Represent the borad
   *  7:0 * * * * * * 7:7
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *  0:0 * * * * * * 0:7
   */
  board: Square[] = [];

  /** Alive pawns */
  pawns:Pawn[];

  /**Selected pawn */
  selectedPawn:Pawn

  /**Square size in px */
  squareSize = Constant.squareSize;

  /**Pawn size in px */
  pawnSize = Constant.pawnSize;

  /**True if spinner should be displayed */
  displaySpinner:boolean = false;

  constructor(private route: ActivatedRoute, private gameService: GameService) {
    this.buildBoard();
  }

  ngOnInit() {
    this.displaySpinner = true;
    this.iaCode = this.route.snapshot.paramMap.get('iaCode');
    this.gameService.newGame(this.iaCode).subscribe(
      (res:Pawn[]) => {
          this.gameId = res[0].fk_game_id;
          this.pawns = res;
          this.displaySpinner = false;
        });
    
  }

  /**Square click handler */
  onSquareClick(square:Square){
    if(square.allowed){
      this.displaySpinner = true;
      this.resetColor();
      let pawnToMove = this.findPawnById(this.selectedPawn.id);
      pawnToMove.horizontal_coord = square.horizontalCoord;
      pawnToMove.vertical_coord = square.verticalCoord;
      this.pawns = _.cloneDeep(this.pawns);
      this.gameService.play(this.gameId, this.selectedPawn, square).subscribe( 
        (res:Pawn[]) => {
          this.pawns = res;
          this.pawns = _.cloneDeep(this.pawns)
          this.displaySpinner = false;
        });
    }

  }

  /**Pawn click handler */
  onPawnClick(pawn:Pawn){
    if(pawn.owner == 'player1'){
      this.selectedPawn = pawn;
      this.resetColor();
      this.highlight(new Coord(pawn.vertical_coord, pawn.horizontal_coord));
      this.highlightAllowedCoords(pawn.allowedMove);
    }else if(pawn.owner == 'player2' && this.selectedPawn != undefined && this.selectedPawn != null){
      let destination = new Coord(pawn.vertical_coord, pawn.horizontal_coord);
      this.onSquareClick(this.findSquareByCoord(destination));
    }
  }

  /**
   * Back to origin color and clear allowed squares
   */
  private resetColor(){
    for(let square of this.board){
      square.color = square.originColor;
      square.allowed = false;
    }
    this.board = _.cloneDeep(this.board);
  }

  /**Highlight selected coord*/
  private highlight(coord:Coord){
    let square = this.findSquareByCoord(coord);
    square.color = 'fuchsia'; 
    this.board = _.cloneDeep(this.board);
  }

  /**Highlight allowed coords */
  private highlightAllowedCoords(coords: Coord[]){
    for(let coord of coords){
      let square = this.findSquareByCoord(coord);
      square.color = 'blue'; 
      square.allowed = true;
    }
    this.board = _.cloneDeep(this.board);
  }

  /**Update pawn list with pawn moved from backend */
  private updatePawnList(movedPawn:Pawn){
    let pawn = this.findPawnById(movedPawn.id);
    pawn.horizontal_coord = movedPawn.horizontal_coord;
    pawn.vertical_coord = movedPawn.vertical_coord;
    this.board = _.cloneDeep(this.board);
  }


  /**Find a pawn by id */
  private findPawnById(id:number){
    for(let pawn of this.pawns){
      if(pawn.id === id){
        return pawn;
      }
    }
  }
  /**Find a squar by coordinate */
  private findSquareByCoord(coord:Coord){
    for(let square of this.board){
      if(square.horizontalCoord === coord.horizontalCoord && square.verticalCoord == coord.verticalCoord){
        return square;
      }
    }
  }

  /**Build the board */
  private buildBoard(){
    for (let vertical_coord = 0; vertical_coord < 8; vertical_coord++) {
      for (let horizontal_coord= 0; horizontal_coord < 8; horizontal_coord++) {
        if(vertical_coord % 2 == 0){
          if (horizontal_coord % 2 == 0) {
            this.board.push(new Square('black', vertical_coord, horizontal_coord));
          } else {
            this.board.push(new Square('white', vertical_coord, horizontal_coord));
          }
        }else{
          if (horizontal_coord % 2 == 0) {
            this.board.push(new Square('white', vertical_coord, horizontal_coord));
          } else {
            this.board.push(new Square('black', vertical_coord, horizontal_coord));
          }
        }
      }
    }
  }



}
