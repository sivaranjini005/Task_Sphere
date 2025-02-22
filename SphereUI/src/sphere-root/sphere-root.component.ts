import { Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { AuthenticationService } from '../services/authentication.service';

@Component({
  selector: 'app-sphere-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './sphere-root.component.html',
  styleUrl: './sphere-root.component.css'
})
export class SphereRootComponent {

  authService = inject(AuthenticationService);

  links: any[] = [
    {
      path: 'home',
      navLable: 'Home',
    },
    {
      path: 'tasklist',
      navLable: 'Task List',
    },
    {
      path: 'history',
      navLable: 'History',
    },
  ];

  logOut() {
    this.authService.logOut();
  }
}
