import React from 'react';
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';
import './ImgCarousel.css'
const Pepe = () => {
  const images = [
    'https://cdn.joinnus.com/files/2023/12/hBMneNHM2QzA0vl.jpg',
    'https://cdn.joinnus.com/files/2023/12/hBMneNHM2QzA0vl.jpg',
    'https://cdn.joinnus.com/files/2023/11/7QNSb2cSvvN4aZz.jpeg',
    'https://cdn.joinnus.com/files/2023/12/hBMneNHM2QzA0vl.jpg',
    'https://cdn.joinnus.com/files/2023/12/vS3WbyyJeiHkKli.PNG',
  ];

  const responsive = {
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 1,
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 1,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1,
    },
  };

  return (
    <Carousel responsive={responsive} 
    itemClass="image-item"
    infinite
    autoPlay 
    autoPlaySpeed={100000}
    showDots={true}
    transitionDuration={500}
    
    draggable={true}
    swipeable={true}
     >
      {images.map((image, index) => (
        <div key={index} className='divcarousel' >
          <img src={image} draggable="false" alt={`Image ${index + 1}`} />
        </div>
      ))}
    </Carousel>
  );
};

export default Pepe;
