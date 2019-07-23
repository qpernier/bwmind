import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Square } from '../models/square';
import { GameService } from './game.service';
import { Pawn } from '../models/pawn';
import { Urls, Constant } from '../constant';

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

  /**Build the board */
  private buildBoard(){
    for (let i = 0; i < 8; i++) {
      for (let y = 0; y < 8; y++) {
        // 7-1 to convert vertical coord to top
        let vertical_coord = (7-i)*this.squareSize;
        let horizontal_coord = y*this.squareSize;
        if(i % 2 == 0){
          if (y % 2 == 0) {
            this.board.push(new Square('black', vertical_coord, horizontal_coord));
          } else {
            this.board.push(new Square('white', vertical_coord, horizontal_coord));
          }
        }else{
          if (y % 2 == 0) {
            this.board.push(new Square('white', vertical_coord, horizontal_coord));
          } else {
            this.board.push(new Square('black', vertical_coord, horizontal_coord));
          }
        }
      }
    }
  }



}
