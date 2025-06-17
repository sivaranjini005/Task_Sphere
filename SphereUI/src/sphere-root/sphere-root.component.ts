import { Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { AuthenticationService } from '../services/authentication.service';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-sphere-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive, MatIconModule],
  templateUrl: './sphere-root.component.html',
  styleUrl: './sphere-root.component.css'
})
export class SphereRootComponent {

  authService = inject(AuthenticationService);

  links: any[] = [
    {
      path: 'home',
      navLable: 'Home',
      icon: 'home'
    },
    {
      path: 'tasklist',
      navLable: 'Task List',
      icon: 'list'
    },
    {
      path: 'history',
      navLable: 'History',
      icon: 'history'
    },
  ];

  logOut() {
    this.authService.logOut();
  }
}
