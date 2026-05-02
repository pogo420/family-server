import { TestBed } from '@angular/core/testing';

import { EventTrackerService } from './event-tracker.service';

describe('EventTrackerService', () => {
  let service: EventTrackerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EventTrackerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
