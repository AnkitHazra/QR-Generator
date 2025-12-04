document.addEventListener('DOMContentLoaded', ()=>{
const clearBtn = document.getElementById('clearBtn')
const copyBtn = document.getElementById('copyBtn')
const linkInput = document.getElementById('link')


if(clearBtn) clearBtn.addEventListener('click', ()=>{ linkInput.value = '' })


if(copyBtn) copyBtn.addEventListener('click', async ()=>{
const img = document.getElementById('qrImg')
if(!img) return
try{
await navigator.clipboard.writeText(img.src)
copyBtn.textContent = 'Copied!'
setTimeout(()=> copyBtn.textContent = 'Copy Image URL', 1500)
}catch(e){
alert('Unable to copy — try manually')
}
})
})