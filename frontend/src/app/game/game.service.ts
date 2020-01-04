import { Injectable } from '@angular/core';
import { Urls } from '../constant';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Pawn } from '../models/pawn';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Coord } from '../models/coord';
import { Square } from '../models/square';
import { parseWebDriverCommand } from 'blocking-proxy/built/lib/webdriver_commands';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json',
    })
  };


  constructor(private http: HttpClient, ) { }

  /**
   * Create new game
   */
  newGame(iaCode: string): Observable<Pawn[]|string> {
    return this.http.get<Pawn[]|string>(Urls.newGame + iaCode).pipe(
      map(this.dictToPawn)
    );
  }

  /**
   * 
   * @param pawn Move a pawn to target square and get the player2 move from backend
   * @param square 
   */
  play(gameId: number, pawn:Pawn, square:Square):Observable<string|Pawn[]>{
    return this.http.post(Urls.play, 
      {"game_id": gameId, "pawn_id": pawn.id, "vertical_coord": square.verticalCoord, "horizontal_coord": square.horizontalCoord}
      ,this.httpOptions).pipe(
        map(this.dictToPawn)
      );
  }

  /**
   * Convert http response datas to a list of pawns with allowed moves
   */
  private dictToPawn(pawnDict):Pawn[]|string{
    if (pawnDict == "player1" || pawnDict == "player2" || pawnDict == "draw"){
      return pawnDict;
    }

    let pawnList:Pawn[] = []; 
    for (let pawn of pawnDict) {
      let allowedMoves = [];
      if (pawn['allowed_move'] !== null && pawn['allowed_move'] !== undefined) {
        for (let allowed_move_row of pawn['allowed_move']) {
          allowedMoves.push(new Coord(allowed_move_row["vertical_coord"], allowed_move_row["horizontal_coord"]))
        }
      }
      pawnList.push(new Pawn(pawn['id'], pawn['owner'], pawn['fk_game_id'], pawn['code'], pawn['vertical_coord'], pawn['horizontal_coord'], allowedMoves));
    }
    return pawnList;
  }
}