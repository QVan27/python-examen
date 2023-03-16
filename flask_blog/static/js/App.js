export default class App {
    constructor() {
        this.el = document.querySelector('body')

        this.getElems()
        this.events()
    }

    getElems() {
        this.$main = this.el.querySelector('main')
        this.$title = this.el.querySelector('.title h1')
        this.$list = this.el.querySelector('.list')
    }

    events() {
        this.$main.addEventListener('load', this.onLoadAnimations())
    }

    onLoadAnimations() {
        this.tl = gsap.timeline({
            paused: true,
            defaults: {
                ease: 'Sine.easeInOut'
            }
        })

        this.tl
            .from(this.$list, { duration: 1, opacity: 0, scale: 0.5 })
            .from(this.$title, { duration: 1, y: 100, opacity: 0 }, '-=0.5')

        this.tl.play()
    }
}
