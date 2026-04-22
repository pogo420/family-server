import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./components/home/home.component').then(m => m.HomeComponent)
    },
    {
        path: 'event-tracker',
        loadComponent: () => import('./components/event-tracker/event-tracker.component').then(m => m.EventTrackerComponent)
    }
];
