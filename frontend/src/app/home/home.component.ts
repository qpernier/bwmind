import { Component, OnInit } from '@angular/core';
import { IA } from '../models/ia.model';
import { IasService } from './ias.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  /** Display the dialog to select the IA */
  displayDialogIASelection: boolean = false;

  selectedIA: string = null;

  /** List the IA ready to play  */
  iaList: IA[] = [];

  constructor(private iasService: IasService, private router: Router) { }

  ngOnInit() {
    this.iasService.getIas().subscribe(res => {
    this.iaList = res;
    });

  }

  onShowDialog() {
    this.displayDialogIASelection = true;
  }

  /**
   * Handle click on the start playing button
   */
  onStartGame() {
    this.router.navigateByUrl('game/' + this.selectedIA);
  }
}
