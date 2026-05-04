import { ChangeDetectorRef, Component } from '@angular/core';
import { EventTrackerService } from '../../../services/event-tracker.service';
import { Event } from '../../../models/event_tracker';
import {MatListModule} from '@angular/material/list';


@Component({
  selector: 'app-show-latest',
  imports: [MatListModule],
  templateUrl: './show-latest.component.html',
  styleUrl: './show-latest.component.css',
})
export class ShowLatestComponent {

  protected events: Event[] = [];
  constructor(private eventService: EventTrackerService, private cd: ChangeDetectorRef) { }

  ngOnInit() {
    this.showLatestEvent();
  }

  private showLatestEvent() {
    const today = new Date();
    const day = today.getDate();        // 1–31
    const month = today.getMonth() + 1; // 0–11, so +1

    console.log(`Fetching events for date: ${day}/${month}`);
    this.eventService.showEventByDate(day, month).subscribe({
        next: (data) => {
          console.log('fetched event data:', data);
          this.events = data;
          this.cd.markForCheck();
        },
        error: (err) => console.error(err),
        complete: () => console.log('fetched event data successfully')
      });
  }


}
