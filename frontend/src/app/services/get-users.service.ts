import { Injectable, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { UsersApiService } from './users-api.service';
import { User } from '../users/user.model';

@Injectable({
  providedIn: 'root'
})
export class GetUsersService implements OnDestroy {
  public usersListSubs: Subscription;
  public usersList: User[];

  constructor(private usersApi: UsersApiService) {}

  public get() {
    this.usersListSubs = this.usersApi.getUsers().subscribe(res => {
      this.usersList = res;
    }, console.error);
  }

  public ngOnDestroy() {
    this.usersListSubs.unsubscribe();
  }
}
