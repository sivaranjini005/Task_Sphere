import { Routes } from '@angular/router';
import { MainSectionComponent } from '../components/main-section/main-section.component';

export const routes: Routes = [
    {
        path: '',
        redirectTo: '/Home',
        pathMatch: 'full'
    },
    {
        path: 'Home',
        component: MainSectionComponent
    },
    {
        path: 'TaskList',
        component: MainSectionComponent
    },
    {
        path: 'Completed',
        component: MainSectionComponent
    },
];
