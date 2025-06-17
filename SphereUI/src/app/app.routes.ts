import { Routes } from '@angular/router';
import { LoginComponent } from '../components/login/login.component';
import { SphereRootComponent } from '../sphere-root/sphere-root.component';
import { HomeComponent } from '../components/home/home.component';
import { TaskListComponent } from '../components/task-list/task-list.component';
import { HistoryComponent } from '../components/history/history.component';
import { authGuard } from '../guards/auth.guard';
import { SignupComponent } from '../components/signup/signup.component';
export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  {
    path: '',
    component: SphereRootComponent,
    canActivate: [authGuard], 
    canActivateChild: [authGuard],
    children: [
      { path: '', redirectTo: 'home', pathMatch: 'full' },
      { path: 'home', component: HomeComponent },
      { path: 'tasklist', component: TaskListComponent },
      { path: 'history', component: HistoryComponent },
      { path: '', redirectTo: 'home', pathMatch: 'full' },
    ],
  },
  { path: '**', redirectTo: '/login' },
];
