import { TestBed } from '@angular/core/testing';

import { IasService } from './ias.service';

describe('IasService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: IasService = TestBed.get(IasService);
    expect(service).toBeTruthy();
  });
});
