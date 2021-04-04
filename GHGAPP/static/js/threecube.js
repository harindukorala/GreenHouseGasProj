$(document).ready(function () {
    setInterval(function() {
    animate();
    }, 5 * 1000);
});

var camera, scene, renderer, container, controls;
var angle = 0;
var radius = 500; 

init();
render();
animate();

function init() {

    scene = new THREE.Scene();
    container = document.getElementById("3dtruckId");
    scene.background = new THREE.Color( 0xa0a0a0 );
    scene.fog = new THREE.Fog( 0xa0a0a0, 10, 500 );

    camera = new THREE.PerspectiveCamera( 65, 792/400, 1, 1000 );
    camera.position.set( - 50, 40, 50 );
    //camera.position.set( 1, 1, 1 );
    scene.add( camera );

    var hemiLight = new THREE.HemisphereLight( 0xffffff, 0x444444 );
    hemiLight.position.set( 0, 100, 0 );
    scene.add( hemiLight );

    var dirLight = new THREE.DirectionalLight( 0xffffff );
    dirLight.position.set( - 0, 40, 50 );
    dirLight.castShadow = true;
    dirLight.shadow.camera.top = 50;
    dirLight.shadow.camera.bottom = - 25;
    dirLight.shadow.camera.left = - 25;
    dirLight.shadow.camera.right = 25;
    dirLight.shadow.camera.near = 0.1;
    dirLight.shadow.camera.far = 200;
    dirLight.shadow.mapSize.set( 1024, 1024 );
    scene.add( dirLight );

    var loader = new THREE.GLTFLoader().setPath( '/static/models/' );
    loader.load( '/static/models/scene.gltf', function ( gltf ) {
        scene.add( gltf.scene );
        render();
    }, undefined, function(error){
        console.error(error);
    });

    var ground = new THREE.Mesh( new THREE.PlaneBufferGeometry( 1000, 1000 ), new THREE.MeshPhongMaterial( { color: 0x999999, depthWrite: false } ) );
    ground.rotation.x = - Math.PI / 2;
    ground.position.y = 11;
    ground.receiveShadow = true;
    scene.add( ground );

    //

    renderer = new THREE.WebGLRenderer( { antialias: true } );
    //renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( 790, 400 );
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.appendChild( renderer.domElement );

    //

    controls = new THREE.OrbitControls( camera, renderer.domElement );
    controls.addEventListener( 'change', render );
    controls.minDistance = 50;
    controls.maxDistance = 200;
    controls.enablePan = false;
    controls.target.set( 0, 20, 0 );
    //controls.autoRotate = true;
    controls.update();

}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
    render();
}


function render() {
    renderer.render( scene, camera );
}

function animate() {
	//requestAnimationFrame( animate );
    camera.position.x = radius * Math.cos( angle );  
    camera.position.z = radius * Math.sin( angle );
    //angle += 0.01;
    angle += 10;
    controls.update();
	renderer.render( scene, camera );
}

