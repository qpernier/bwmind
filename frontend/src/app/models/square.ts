import { Constant } from '../constant';

export class Square{
    public top: string;
    public left: string;
    public originColor: string;
    public allowed:boolean = false;
    constructor(public color: string, public verticalCoord: number, public horizontalCoord: number){
        this.top = ((7 - this.verticalCoord) * Constant.squareSize) + 'px';
        this.left = (this.horizontalCoord * Constant.squareSize) + 'px';
        this.originColor = this.color;
    }
}