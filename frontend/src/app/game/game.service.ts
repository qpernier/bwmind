import { Injectable } from '@angular/core';
import { Urls } from '../constant';
import { HttpClient } from '@angular/common/http';
import { Pawn } from '../models/pawn';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(private http: HttpClient,) { }

  /**
   * Create new game
   */
  newGame(iaCode: string): Observable<Pawn[]>{
    return this.http.get<Pawn[]>(Urls.newGame + iaCode).pipe(
      map( pawnDict => { 
        let pawnList = [];
        for (let pawn of pawnDict){
          pawnList.push(new Pawn(pawn['id'], pawn['owner'], pawn['fk_game_id'], pawn['code'], pawn['vertical_coord'], pawn['horizontal_coord']));
        }
        return pawnList;
    }),
    );
  }
}