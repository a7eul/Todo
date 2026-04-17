document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(15px)";

        setTimeout(() => {
            card.style.transition = "all 0.4s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 80);
    });

});
document.addEventListener("DOMContentLoaded", () => {

    const dropdowns = document.querySelectorAll(".dropdown");

    dropdowns.forEach(drop => {
        const btn = drop.querySelector(".dropdown-toggle");

        btn.addEventListener("click", (e) => {
            e.stopPropagation();

            document.querySelectorAll(".dropdown").forEach(d => {
                if (d !== drop) d.classList.remove("active");
            });

            drop.classList.toggle("active");
        });
    });

    document.addEventListener("click", () => {
        document.querySelectorAll(".dropdown").forEach(d => {
            d.classList.remove("active");
        });
    });

});

function changeStatus(taskId) {
  const form = document.getElementById(`status-form-${taskId}`);
  if (!form) return;
  
  const select = form.querySelector('select');
  const originalValue = select.value;
  
  select.disabled = true;
  select.style.opacity = '0.6';
  
  const formData = new FormData(form);
  
  fetch(form.action, {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': formData.get('csrfmiddlewaretoken')
    }
  })
  .then(response => {
    if (response.ok || response.redirected) {
      window.location.reload();
    } else {
      select.value = originalValue;
      alert('Ошибка при изменении статуса');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    select.value = originalValue;
    select.disabled = false;
    select.style.opacity = '1';
    alert('Произошла ошибка');
  });
}

document.querySelectorAll('.dropdown-toggle').forEach(button => {
  button.addEventListener('click', function(e) {
    e.stopPropagation();
    const dropdown = this.closest('.dropdown');
    const menu = dropdown.querySelector('.dropdown-menu');
    
    document.querySelectorAll('.dropdown').forEach(d => {
      if (d !== dropdown) d.classList.remove('active');
    });
    
    dropdown.classList.toggle('active');
  });
});


document.addEventListener('click', function(e) {
  if (!e.target.closest('.dropdown')) {
    document.querySelectorAll('.dropdown').forEach(d => {
      d.classList.remove('active');
    });
  }
});


function changeStatus(taskId) {
    const form = document.getElementById(`status-form-${taskId}`);
    if (!form) return;
    
    const select = form.querySelector('select');
    const originalValue = select.value;
    

    select.disabled = true;
    select.style.opacity = '0.6';
    
    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
    .then(response => {
        if (response.ok || response.redirected) {
            window.location.reload(); 
        } else {
            select.value = originalValue; 
            alert('Ошибка при изменении статуса');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        select.value = originalValue;
        select.disabled = false;
        select.style.opacity = '1';
        alert('Произошла ошибка. Попробуйте ещё раз.');
    });
}