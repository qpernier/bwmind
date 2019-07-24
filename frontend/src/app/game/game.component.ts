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

  constructor(private route: ActivatedRoute, private gameService: GameService) {
    this.buildBoard();
  }

  ngOnInit() {
    this.iaCode = this.route.snapshot.paramMap.get('iaCode');
    this.gameService.newGame(this.iaCode).subscribe(
      res => {
          this.pawns = res;
          console.log(this.pawns);
        });
    
  }

  /**Square click handler */
  onSquareClick(square:Square){
    if(square.allowed){
      this.resetColor();
      //TODO ajouter (click) html
      // deplacer pion sur cette case.
      //todo service qui deplace le pion en bdd et appelle l'ia
    }

  }

  /**Pawn click handler */
  onPawnClick(pawn:Pawn){
    if(pawn.owner == 'player1'){
      this.selectedPawn = pawn;
      this.resetColor();
      this.highlight(new Coord(pawn.vertical_coord, pawn.horizontal_coord));
      this.highlightAllowedCoords(pawn.allowedMove);
    }
  }

  /**Back to origin color */
  private resetColor(){
    for(let square of this.board){
      square.color = square.originColor;
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
