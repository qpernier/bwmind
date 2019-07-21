import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Urls } from '../constant';
import { IA } from '../models/ia.model';


@Injectable({
  providedIn: 'root'
})
export class IasService {

  constructor(private http: HttpClient,) { }

  /** GET ias from the server */
  getIas(): Observable<IA[]> {
    return this.http.get<[]>(Urls.ias).pipe(
      map(raws => {
          let IAList:IA[] = [];
          for(let raw of raws){
            IAList.push(new IA(raw['pk'],raw['fields']['name'],raw['fields']['code']));
          }
          return IAList;
          }
         )
      );
  }
}
