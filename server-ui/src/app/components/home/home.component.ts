import { ChangeDetectionStrategy, Component } from '@angular/core';  
import { NavBarComponent } from '../nav-bar/nav-bar.component';
import { ShowLatestComponent } from '../event-tracker/show-latest/show-latest.component';
import { MatDividerModule } from '@angular/material/divider';



@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    NavBarComponent,
    ShowLatestComponent
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HomeComponent {

  protected readonly homePageContent = `
    Welcome to family server UI.
    <br>Select the menu for appropriate actions.
    <br>For any queries/questions please contact server admins.
  `;

}
