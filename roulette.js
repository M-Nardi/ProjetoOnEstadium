const items = [
'mouse.png',
'bag.png',
'monitor.png',
'mouse.png',
'placa.png',
'monitor.png',
'mouse.png',
'bag.png',
'placa.png',
'mouse.png',
'placa.png',
'mouse.png',
'mouse.png',
'placa.png',
'bag.png',
'monitor.png',
'mouse.png',
'placa.png',
'placa.png',
'mouse.png',
'bag.png',
'bag.png',
'placa.png',
'mouse.png',
'monitor.png',
'placa.png',
'mouse.png',
'mouse.png',
'placa.png',
'mouse.png',
'placa.png',
'placa.png',
    
];


const premio = [
'mousepremio.png',
'bagpremio.png',
'monitorpremio.png',
'mousepremio.png',
'placapremio.png',
'monitorpremio.png',
'mousepremio.png',
'bagpremio.png',
'placapremio.png',
'mousepremio.png',
'placapremio.png',
'mousepremio.png',
'mousepremio.png',
'placapremio.png',
'bagpremio.png',
'monitorpremio.png',
'mousepremio.png',
'placapremio.png',
'placapremio.png',
'mousepremio.png',
'bagpremio.png',
'bagpremio.png',
'placapremio.png',
'mousepremio.png',
'monitorpremio.png',
'placapremio.png',
'mousepremio.png',
'mousepremio.png',
'placapremio.png',
'mousepremio.png',
'placapremio.png',
'placapremio.png',
];









class Roulette {

    constructor() {
        this.SIZE = 128;
        this.LENGTH = 80;
        this.DURATION = 10000;

        this.progress = 0;

        this.startTime = 0;
        this.lastItem = 0;

        this.level = 0;
        
        this.roulette = document.getElementById("roulette");
        this.items = this.roulette.children;
    }

    init(images) {
        if (!Array.isArray(images)) {
            console.log("necessita de imagem para ser rodado");
        }

        images.forEach(src => {
            const img = new Image();
            img.src = src;
        });

        for (let i = 0; i < 11; i++) {
            const item = this.items[i];
            
            item.style.position = 'absolute';
            item.style.transform = `translateX(${i * this.SIZE}px)`;
            item.lastChild.src = this.getItem();
        }
    }

    start(lastItem) {
        this.level = 0;
        this.progress = 0;
        this.lastItem = lastItem;
        this.startTime = Date.now();
        

        for (let i = 0; i < 11; i++) {
            this.items[i].value = 0;
            
        }
        
        
        window.requestAnimationFrame(() => this.update());
    }

    update() {
        this.progress = (Date.now() - this.startTime) / this.DURATION;
        
        if (this.progress > 1) {
            this.progress = 1;
            this.render();
            
            
            return;
        }

        this.render();
        

        window.requestAnimationFrame(() => this.update());
    }

    render() {
        const off = this.interpolator(this.progress) * this.SIZE * this.LENGTH;
        const WIDTH = this.SIZE * 11;

        for (let i = 0; i < 11; i++) {
            const item = this.items[i];
            const base = (i + 1) * this.SIZE - off;
            const index = -Math.floor(base / WIDTH);
            const value = ((base % WIDTH) + WIDTH) % WIDTH - this.SIZE;
            
            item.style.transform = `translateX(${value}px)`;

            if (item.value != index) {
                this.level += index - item.value;
                
                item.value = index;
                item.lastChild.src = this.getItem();
                

                if (this.level == this.LENGTH - 6) {
                    item.lastChild.src = this.getItem(this.lastItem);
                }
            }
        }
    }

    interpolator(val) {
        return Math.pow(Math.sin(val * Math.PI / 2), 2.6);
    }

    
    getItem(val) {
        val = typeof val !== "undefined" ? val : Math.floor(Math.random() * items.length);
        return items[val];
        
        
    }
	

    	
    
}



var contador = 0
var audio2 = new Audio("Sounds/tone.wav");
var audio4 = new Audio("Sounds/end.mp3");

function playwin(){
	var audio = new Audio("Sounds/rolling.mp3");
	audio.play();
	var audio3 = new Audio("Sounds/roll.mp3");
    audio3.play();
	myVar = setTimeout(function(){ audio2.play() }, 10000);
	myVar = setTimeout(function(){ audio4.play() }, 10100);
    document.querySelector("#premio").innerHTML = '<img id="theImg" src="'+premio[contador]+'" />';
    console.info(contador);
	contador++;
};




const roulette = new Roulette();
roulette.init(items);


const btnStart = document.getElementById("roulette-start");
const selectWinner = document.getElementById("roulette-select-winner");


btnStart.onclick = () => roulette.start(parseInt(selectWinner.value++, 10));