/**
 * Get the current coordinates of a DOM element.
 * @param {Element} element - The position to scroll to.
 * @return {object} Object containing the coordinates of the considered element.
 */
function getElementOffset(element) {
  const de = document.documentElement;
  const box = element.getBoundingClientRect();
  const top = (box.top + window.pageYOffset) - de.clientTop;
  const left = (box.left + window.pageXOffset) - de.clientLeft;
  return { top, left };
}

export default getElementOffset;
