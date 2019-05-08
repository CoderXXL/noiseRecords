import { Component, OnInit } from '@angular/core';
import { GetUsersService } from '../services/get-users.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  constructor(public getUsers: GetUsersService) {
    this.getUsers.get();
  }

  ngOnInit() {}
}
