let bird = document.getElementById("bird");
let box = document.getElementById("birdbox");
/* Make a Bird Move Inside The bar */
let pixls = 0;
let togle = true;
let Bird_Anmiation = setInterval(()=> 
  {
    /* the Togle Use Is To Know When Change Diraction */
    if ( togle == true)
    {
      pixls = pixls + 2 ;
      /* To Make The Bird Movement Related to Box width aka To Be Usable For any Device. */
      if (pixls >= box.clientWidth-80)
      {togle = false ;
      bird.style.cssText = 'transform: rotatey(0deg);  ';}
    }

    if ( togle == false) {
      pixls = pixls-2;
      if (pixls <= 0)
     { togle = true ;
      bird.style.cssText = 'transform: rotatey(180deg);  ';}
    }
    /* move the bird BY pixls */
    move(pixls);
  }, 20);
/* evry 20 ms the bird move 2 px */
function move(pixls) 
  {
  bird.style.left = pixls  + 'px';
  }
/* Here We End Bird Movements */ 


/* Dynamically build the sections menue */
let Sections = document.querySelector("#sections_box");
let SectionName = document.querySelectorAll(".section_name")
let SectionsList = document.createElement("ul")
SectionsList.style.listStyle="none";
let ID=[];
let index = 0;
/** For Claer Interval */
function clearThis(I)
{
  clearInterval(ID[I]);
};
/** For Adding Li Element For Each Section in Menue */
for (let sec of SectionName) 
{
  let list = document.createElement("li");
  let pos;
  list.classList.add("button");
  list.innerHTML=`${sec.innerHTML}`;
  /** Adding Event Listener For Each List Item  */
  list.addEventListener("click", ()=>
  {
    /** to prevent error that occure when click another sections while scrolling to another */   
    for (let i = 0; i <= index ; i++)
    {
      clearThis(i)
    }
    ID[index]=setInterval(()=>{
      pos = sec.getBoundingClientRect();
      if (pos['y'] >= 70)
      {
        window.scrollBy(0,5);    
        if (pos['y'] <= 78 )
        {
          
          clearThis(index);
        };
      }
      else if (pos['y']<=70)
      {
        window.scrollBy(0,-5); 
        if (pos['y'] >= 63 )
        {
          clearThis(index);
        };
      }  
      let EOFPage = document.body.getBoundingClientRect();
      const height = window.innerHeight;
      if (EOFPage['bottom'] <= height-10)
      {
        for (let i = 0; i <= index ; i++)
        {
          clearThis(i)
        }
      }
    },5)})
  index+=1;
  SectionsList.appendChild(list)
}
Sections.appendChild(SectionsList);


// To Show and Hide Sections Slide Box 
let select = document.querySelectorAll(".button");
Sections.addEventListener("mouseover" ,  () =>
{
  for (let i = 2 ; i <= index+1 ; i++)
  {
    select[i].style.display = "block";
  }
});
Sections.addEventListener("mouseleave" , () =>
{
  for (let i = 2 ; i <= index+1 ; i++)
  {
    select[i].style.display = "none"; 
  }
});


// To Let Home Buuton Lead To Top of The Page
let home = document.querySelector("#home");
home.addEventListener("click",() => 
  {
    scroll(0,0)
  })


// To Show The Bar While Going Up And Hide While Going Down
let TheBar = document.querySelector("#selector");
let selections = document.querySelectorAll(".section");
let yindx = window.scrollY;
let ulist = document.querySelectorAll("li");
document.addEventListener("scroll",()=>
{
  if (yindx >50)
  {
      if (yindx >= window.scrollY+15)
    {
      TheBar.classList.remove("hidden")
    }
    else if (yindx < window.scrollY-15)
    { 
      TheBar.classList.add("hidden")
    }
  }
  let itration = 0 ;
  yindx = window.scrollY;
  for (const sector of selections) {
    let Mypos = sector.getBoundingClientRect();
    let MyTextPos = sector.nextElementSibling.getBoundingClientRect();
    let itrationTwo = 0 ;
    if (Mypos['y'] <=200 && Mypos['y']>=-MyTextPos['height'])
    {
      sector.classList.add("active")
      ulist[itration].classList.add("active")
      for (let sectorTwo of selections) {
        if (itrationTwo != itration)
        {
          sectorTwo.classList.remove("active")
          ulist[itrationTwo].classList.remove("active")
        }
        itrationTwo+=1; 
      }
    }
    itration +=1;
    
  }
})


// To Collabse The Sections
// I Put tog To Detrmine When It Open And When Not
let tog = false ;

for (let selected of selections)
{
  selected.addEventListener("click",() =>
  {
    if (tog == false)
    {
      selected.nextElementSibling.style.display = "none";
      tog = true ;
      selected.style.cssText = 'box-shadow: 2px 2px 5px rgb(0, 0, 0.2);';
    }
    else if (tog == true)
    {
      selected.nextElementSibling.style.display = "block";
      tog = false ;
      selected.style.cssText ='box-shadow: 2px 2px -5px rgb(0, 0, 0.2);';
    }
  });
  // OtherWise Making A new For Loop For Nothing I Used The Same For Loop For Collapsing 
  // To Make Evry Section Button To Head To It's Section (maping) 
}
// Please Comment Me How Could It Be Better Even if This Project Accepted Thanks For You Time 







  
