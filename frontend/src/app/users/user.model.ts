export class User {
  constructor(
    public name: string,
    public description: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string
  ) {}
}
